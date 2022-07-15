from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Parameters(models.Model):
    #Селекторы для полей с выбором
    N_choices = (
        (512, '512'),
        (1024, '1024'),
        (2048, '2048'),
        (4096, '4096'),
        (8192, '8192'),
        (16384, '16384'),
    )
    norm_length_choices = (
        ('L_cp', 'L_cp'),
        ('L_D2', 'L_D2'),
        ('L_D3', 'L_D3'),
        ('L_NL', 'L_NL'),
        ('L_S', 'L_S'),
        ('L_ICS', 'L_ICS'),
    )
    sgn_choices = ((1, '+1'), (-1, '-1'))
    pulse_choices = (
        ('Гауссовский импульс', 'Гауссовский импульс'),
        ('Супергауссовский импульс', 'Супергауссовский импульс'),
        ('Солитоноподобный импульс', 'Солитоноподобный импульс')
    )
    #Внешний ключ на таблицу User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Поля таблицы
    name = models.CharField(max_length=200, verbose_name='Название')
    #Рассчетная область
    T = models.FloatField(verbose_name='Размер T')
    N = models.IntegerField(verbose_name='Число точек', choices=N_choices, default=1024)
    norm_length = models.CharField(max_length=5, verbose_name='Нормирующая длина', choices=norm_length_choices, default='L_cp')
    L = models.FloatField(verbose_name='Размер')
    N1 = models.IntegerField(verbose_name='Число точек дискретизации')
    #Характеристики среды
    muFD2 = models.FloatField(verbose_name='Дисперсия второго порядка')
    sgn2 = models.IntegerField(verbose_name='Знак дисперсии второго порядка', choices=sgn_choices)
    muFD3 = models.FloatField(verbose_name='Дисперсия третьего порядка')
    sgn3 = models.IntegerField(verbose_name='Знак дисперсии третьего порядка', choices=sgn_choices)
    muFN = models.FloatField(verbose_name='Фазовая самомодуляция')
    muFs = models.FloatField(verbose_name='Ударная волна огибающей')
    muFL = models.FloatField(verbose_name='Вынужденное комбинационное саморассеяние')
    alpha0 = models.FloatField(verbose_name='Потери')
    # Входной импульс
    pulse = models.CharField(max_length=24, verbose_name='Форма импульса', choices=pulse_choices)
    ccf = models.FloatField(verbose_name='Частотная модуляция C')
    mcf = models.FloatField(verbose_name='Крутизна фронта m')