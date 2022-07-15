import numpy as numpy

"""### ЗАДАНИЕ ПАРАМЕТРОВ ЭКСПЕРИМЕНТА ###"""

# Параметры супергаусовского импульса: m, C (для солитоноподобного импульса - коэффициент C)
# mcf = 1
# ccf = 0
# #Параметры временной оси: размер T и количество точек дискретизации N
# T = 56
# N = 2**10
#
# #Шаг временной оси dT
# dT = T/(N-1)
#
# #Параметры пространственной оси
# L = 1*numpy.pi  #Длина волокна
# N1 = 5000       #Количество точек дискретизации
# st = L/(N1-1)   #Шаг пространственной оси
# koeff = 50      #Коэффициент "прореживания" точек по пространственной оси
#
# #Коэффициенты в уравнении (параметры среды)
# sgn1 = -1   #Знак дисперсии второго порядка
#
# muFD = 0    #L_NL / L_D      дисперсия второго порядка
# muFD3 = 0.1 #L_NL / L_D3     дисперсия третьего порядка
# muFs = 0    #L_NL / L_shock  ударная волна
# muFL = 0    #L_NL / L_last   последнее слагаемое (самосмещение частоты)
# alpha0 = 0   #коэффициент потерь


"""### ВЫЧИСЛИТЕЛЬНОЕ ЯДРО ###"""

def calc(T, N, N1, L, muFD2, sgn2, muFD3, sgn3, muFN, muFs, muFL, alpha0, pulse, ccf, mcf):

    # Шаг временной оси dT
    dT = T / (N - 1)

    st = L / (N1 - 1)  # Шаг пространственной оси
    koeff = 50  # Коэффициент "прореживания" точек по пространственной оси

    #Формирование входного импульса
    ii = numpy.arange(0, N)
    time = -T/2 + ii*T/(N-1)

    #Форма импульса - нужное раскомментировать
    if pulse == 'Солитоноподобный импульс':
        fun = (1 / numpy.cosh(time)) * numpy.exp(-0.5j * ccf * (time ** 2)) #Солитоноподобный импульс
    else:
        fun = numpy.exp(-(1 + 1j * ccf) * time ** (2 * mcf) / 2)  # Супергауссовский импульс
    res = fun[1:]*numpy.conj(fun[1:])
    #Формирование массива частот для использования при преобразовании Фурье
    OMEGA = 2*numpy.pi*(N-1)/T  #Интервал частот
    dom = OMEGA/(N-1)           #Шаг дискретизации по частоте
    #Основной массив частот для численного расчёта
    om = numpy.append([], dom*numpy.arange(0, N/2))
    om = numpy.append(om, -dom*numpy.arange(N/2, 0, -1))
    #Вспомогательный массив частот для визуализации спектра
    omscale = om[int(N/2):]
    omscale = numpy.append(omscale, om[0:int(N/2)])

    #Формирование массива времени для оценки интегральной интенсивности
    tscale = numpy.array([-T/2+(i-1)*T/(N-1) for i in range(1, N + 1)])

    #Формирование массива значений оператора дисперсии для использования при преобразовании Фурье

    #ВИД D_ ЗАВИСИТ ОТ ВАРИАНТА
    D_ = (1j/2)*sgn2*muFD2*om*om - (1j/6)*sgn3*muFD3*om*om*om

    #ВИД De ОТ ВАРИАНТА НЕ ЗАВИСИТ
    De = numpy.exp(st*D_/2)


    # *************************
    # **  РЕШЕНИЕ УРАВНЕНИЯ  **
    # *************************

    #Инициализация счётчиков шагов
    kk = 0
    kk2 = 0

    #Текущее значение амплитуды
    curfun = fun[:]

    #Первое преобразование Фурье
    ffun = numpy.fft.fft(curfun)

    #"Проходим" по волокну (начало цикла по i - по длине волокна)
    for i in range(1, N1):
        #ДИСПЕРСИЯ. ШАГ 1
        temp = ffun*De                  #Действие оператора дисперсии
        curfun2 = numpy.fft.ifft(temp)  #Обратное преобразование Фурье

        #НЕЛИНЕЙНОСТЬ
        #Вычисление текущей координаты
        x = (i - 1)*st

        #Вычисление производных dA/dt и d(A*)/dt
        #для учёта слагаемого ударной волны и учёта последнего слагаемого
        # dA/dt
        dif = [(curfun2[1] - curfun2[0])/dT,]
        dif = numpy.append(dif, (curfun2[2:] - curfun2[0:-2])/(2*dT))
        dif = numpy.append(dif, [(curfun2[-1] - curfun2[-2])/dT,])
        #d(A*)/dt
        difc = [(numpy.conj(curfun2[1]) - numpy.conj(curfun2[0])) / dT ]
        difc = numpy.append(difc, (numpy.conj(curfun2[2:]) - numpy.conj(curfun2[0:-2])) / (2 * dT))
        difc = numpy.append(difc, [(numpy.conj(curfun2[-1]) - numpy.conj(curfun2[-2])) / dT])
        #Вычисление оператора нелинейности
        #ВИД ОПЕРАТОРА ЗАВИСИТ ОТ ВАРИАНТА
        NL = muFN*1j*numpy.exp(-alpha0*x)*curfun2*numpy.conj(curfun2) - \
            muFs*numpy.exp(-alpha0*x)*(curfun2*difc + 2*numpy.conj(curfun2)*dif) - \
            1j*muFL*numpy.exp(-alpha0*x)*(curfun2*difc + numpy.conj(curfun2)*dif)

        #Новое значение функции после учёта нелинейности
        curfun3 = numpy.exp(st*NL)*curfun2

        #ДИСПЕРСИЯ. ШАГ 2
        ffun = numpy.fft.fft(curfun3)   #Преобразование Фурье
        temp = ffun*De                  #Действие оператора дисперсии
        curfun = numpy.fft.ifft(temp)   #Обратное преобразование Фурье
        ffun = temp                     #Запоминаем значение temp, чтобы избежать лишнего преобразования

        #Увеличение счётчика шагов
        kk = kk + 1

        #Запоминаем решение в соответствии с коэффициентом прореживания
        if kk == koeff:
            kk2 = kk2 + 1
            fun = numpy.vstack((fun, curfun))
            sum_p = numpy.trapz(curfun*numpy.conj(curfun), x=tscale)
            kk = 0
    #Конец цикла

    #Формирование массива пространственной шкалы для визуализации
    #и учёт потерь при нормировке амплитуды
    zscale = []
    sum_p = []
    for i in range(1, kk2 + 2):
        zscale = numpy.append(zscale, (1 + koeff*(i - 1))*st)
        fun[i-1] = fun[i-1]*numpy.exp(-alpha0*zscale[i-1]/2)
        sum_p = numpy.append(sum_p, numpy.trapz(fun[i-1]*numpy.conj(fun[i-1]), x = tscale))

    #Вычисление интенсивности
    res = fun*numpy.conj(fun)

    #Вычисление формы спектра импульса
    sptemp = fun.T
    spectr = numpy.fft.fftshift(numpy.fft.fft(sptemp, axis=0))
    sptemp = spectr*numpy.conj(spectr)/N
    sptemp2 = sptemp.T
    spres = sptemp2[int(kk2 / 2) + 1:]
    spres = numpy.append(spres, sptemp2[0:int(kk2 / 2 + 1)], axis=0)


    return {
        'zscale': numpy.array(zscale, dtype='float'),
        'sum_p': numpy.array(sum_p, dtype='float'),
        'tscale': numpy.array(tscale, dtype='float'),
        'res': numpy.array(res, dtype='float'),
        'spres': numpy.array(spres, dtype='float'),
        'omscale': numpy.array(omscale, dtype='float'),
    }