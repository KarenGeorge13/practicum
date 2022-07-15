# Generated by Django 3.1.7 on 2021-05-29 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('T', models.FloatField(verbose_name='Размер T')),
                ('N', models.IntegerField(choices=[(512, '512'), (1024, '1024'), (2048, '2048'), (4096, '4096'), (8192, '8192'), (16384, '16384')], default=1024, verbose_name='Число точек')),
                ('norm_length', models.CharField(choices=[('Lcp', 'L_cp'), ('Ld2', 'L_D2'), ('Ld3', 'L_D3'), ('Lnl', 'L_NL'), ('Ls', 'L_S'), ('Lics', 'L_ICS')], default='Lcp', max_length=4, verbose_name='Нормирующая длина')),
                ('L1', models.FloatField(verbose_name='Размер')),
                ('N1', models.IntegerField(verbose_name='Число точек дискретизации')),
                ('muFD2', models.FloatField(verbose_name='Дисперсия второго порядка')),
                ('sgn2', models.IntegerField(choices=[(1, '+1'), (-1, '-1')], verbose_name='Знак дисперсии второго порядка')),
                ('muFD3', models.FloatField(verbose_name='Дисперсия третьего порядка')),
                ('sgn3', models.IntegerField(choices=[(1, '+1'), (-1, '-1')], verbose_name='Знак дисперсии третьего порядка')),
                ('muFN', models.FloatField(verbose_name='Фазовая самомодуляция')),
                ('muFs', models.FloatField(verbose_name='Ударная волна огибающей')),
                ('muFL', models.FloatField(verbose_name='Вынужденное комбинационное саморассеяние')),
                ('alpha0', models.FloatField(verbose_name='Потери')),
                ('impulse', models.IntegerField(choices=[(1, 'Гауссовский импульс'), (2, 'Супергауссовский импульс'), (3, 'Солитоноподобный импульс')], verbose_name='Форма импульса')),
                ('ccf', models.FloatField(verbose_name='Частотная модуляция C')),
                ('mcf', models.FloatField(verbose_name='Крутизна фронта m')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
