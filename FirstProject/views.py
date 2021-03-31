from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from subscribers.models import Subscriber


def show_home(request):
    return render(request, 'index.html')


def show_portfolio(request):
    return render(request, 'portfolio.html')


def do_subscribe(request):
    email = request.POST['email']

    subscriber = Subscriber(email=email)
    subscriber.save()
    return redirect('/')


def do_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in !!!')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('login')

    return render(request, 'login.html')


def do_register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']

        user = User(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()
        messages.success(request, 'Registered Successfully !')
        return redirect('login')

    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
