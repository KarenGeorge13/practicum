from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm, ExperimentForm
from django.contrib.auth import authenticate, login, logout
from .calc import calc
from .charts import *
from .models import Parameters
from sys import getsizeof

# Create your views here.


def index(request):
    return render(request, 'pract/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username=name, password=password, first_name=fname, last_name=lname)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'pract/register.html', {'form': form})


def authen(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'pract/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def user_profile(request, user_id):
    #создать коллекцию сохраненных наборов параметров пользователя
    user = get_object_or_404(User, pk=user_id)
    parameters = Parameters.objects.filter(user=user_id)
    return render(request, 'pract/profile.html', {'user': user, 'parameters': parameters})


def delete_parameter(request, parameter_id):
    parameter = get_object_or_404(Parameters, pk=parameter_id)
    parameter.delete()
    return user_profile(request, request.user.pk)


def methodical_instructions(request):
    return render(request, 'pract/meth.html')


def experiment(request):
    if request.method == 'POST':
        form = ExperimentForm(data=request.POST)
        context = {'form': form, 'is_chart': False}
        if form.is_valid():
            if '_save' in request.POST:
                do_save(form.cleaned_data, request.user)
                redirect('experiment')
            elif '_calc' in request.POST:
                context.update(do_calc(form.cleaned_data))
    else:
        form = ExperimentForm()
        context = {'form': form, 'is_chart': False}
    return render(request, 'pract/experiment.html', context)


def parameter_based_experiment(request, parameter_id):
    parameter = get_object_or_404(Parameters, pk=parameter_id)
    data = {
        'name': parameter.name,
        'T': parameter.T,
        'N': int(parameter.N),
        'norm_length': parameter.norm_length,
        'N1': parameter.N1,
        'L': parameter.L,
        'muFD2': parameter.muFD2,
        'sgn2': int(parameter.sgn2),
        'muFD3': parameter.muFD3,
        'sgn3': int(parameter.sgn3),
        'muFN': parameter.muFN,
        'muFs': parameter.muFs,
        'muFL': parameter.muFL,
        'alpha0': parameter.alpha0,
        'pulse': parameter.pulse,
        'ccf': parameter.ccf,
        'mcf': parameter.mcf
    }
    form = ExperimentForm(data)
    context = {'form': form, 'is_chart': False}
    return render(request, 'pract/experiment.html', context)


def do_calc(data):
    result = calc(
        T=data.get('T'),
        N=int(data.get('N')),
        N1=data.get('N1'),
        L=data.get('L'),
        muFD2=data.get('muFD2'),
        sgn2=int(data.get('sgn2')),
        muFD3=data.get('muFD3'),
        sgn3=int(data.get('sgn3')),
        muFN=data.get('muFN'),
        muFs=data.get('muFs'),
        muFL=data.get('muFL'),
        alpha0=data.get('alpha0'),
        pulse=data.get('pulse'),
        ccf=data.get('ccf'),
        mcf=data.get('mcf'),
    )
    return {
        'integral_intensity': integral_intensity(result['zscale'], result['sum_p']),
        'impulse_shape': impulse_shape(result['tscale'], result['res']),
        'impulse': impulse(result['zscale'], result['tscale'], result['res']),
        'spectrum_shape': spectrum_shape(result['tscale'], result['spres']),
        'spectrum': spectrum(result['omscale'], result['zscale'], result['spres']),
        'is_chart': True
    }


def do_save(data, user):
    parameter = Parameters(
        user=user,
        name=data.get('name'),
        T=data.get('T'),
        N=int(data.get('N')),
        norm_length=data.get('norm_length'),
        N1=data.get('N1'),
        L=data.get('L'),
        muFD2=data.get('muFD2'),
        sgn2=int(data.get('sgn2')),
        muFD3=data.get('muFD3'),
        sgn3=int(data.get('sgn3')),
        muFN=data.get('muFN'),
        muFs=data.get('muFs'),
        muFL=data.get('muFL'),
        alpha0=data.get('alpha0'),
        pulse=data.get('pulse'),
        ccf=data.get('ccf'),
        mcf=data.get('mcf')
    )
    parameter.save()