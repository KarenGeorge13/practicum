from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class ExperimentForm(forms.Form):
    #Рассчетная область
    name = forms.CharField(initial='Набор параметров', widget=forms.TextInput(attrs={'class':'popup-form-control'}))
    T = forms.FloatField(initial=40, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}), min_value=0.0000000001)
    N = forms.ChoiceField(initial=1024, widget=forms.Select(attrs={'class': 'choice-experiment-form-control'}), choices=(
        (512, '512'),
        (1024, '1024'),
        (2048, '2048'),
        (4096, '4096'),
        (8192, '8192'),
        (16384, '16384')
    ))
    norm_length = forms.ChoiceField(initial='Lcp', widget=forms.Select(attrs={'class': 'choice-experiment-form-control', 'onchange':'Changed(true)'}), choices=(
        ('L_cp', 'L_cp'),
        ('L_D2', 'L_D2'),
        ('L_D3', 'L_D3'),
        ('L_NL', 'L_NL'),
        ('L_S', 'L_S'),
        ('L_ICS', 'L_ICS'),
    ))

    L = forms.FloatField(initial=1, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    N1 = forms.IntegerField(initial=2000, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}), min_value=51, max_value=20000)
    #Характеристики среды
    muFD2 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    sgn2 = forms.ChoiceField(initial=1, widget=forms.Select(attrs={'class': 'choice-experiment-form-control'}), choices=((1, '+1'), (-1, '-1')))
    muFD3 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    sgn3 = forms.ChoiceField(initial=1, widget=forms.Select(attrs={'class': 'choice-experiment-form-control'}), choices=((1, '+1'), (-1, '-1')))
    muFN = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    muFs = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    muFL = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control', 'style':'height: 17px;'}))
    alpha0 = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    #Входной импульс
    pulse = forms.ChoiceField(initial='Гауссовский импульс',  widget=forms.RadioSelect(attrs={'name': 'rating', 'oninput':'Selected()', 'class': 'param-label'}),
                                choices=(
                                    ('Гауссовский импульс', 'Гауссовский импульс'),
                                    ('Супергауссовский импульс', 'Супергауссовский импульс'),
                                    ('Солитоноподобный импульс', 'Солитоноподобный импульс')
                                ))
    ccf = forms.FloatField(initial=0, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))
    mcf = forms.FloatField(initial=1, widget=forms.TextInput(attrs={'class': 'small-experiment-form-control'}))

