from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import SignUpForm, AddUserForm, LoginUserForm
from clients.models import Client
from team.models import UserModel


def singin(request):
    if request.user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'team/login.html', {'form': form})


def registration_team(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистированы!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'team/registration.html', {'form': form})


@login_required
def home(request):
    clients = Client.objects.filter(user=request.user).order_by('-data')
    paginator = Paginator(clients, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    workers = UserModel.objects.filter(user=request.user)
    return render(request, 'team/home.html', {'page_obj': page_obj, 'workers': workers})


@login_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.user = request.user
            new_user.save()
            messages.success(request, 'Сотрудник добавлен')
            return redirect('home')
    else:
        form = AddUserForm()
    return render(request, 'team/add_user.html', {'form': form})


def view_user_clients(request, id):
    user_name = UserModel.objects.get(id=id, user=request.user)
    workers = Client.objects.filter(worker=user_name.first_name)

    paginator = Paginator(workers, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'team/view_user.html', {'page_obj': page_obj})


def log_out(request):
    logout(request)
    return redirect('login')
