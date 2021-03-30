from django.contrib import auth
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
            return HttpResponse('User logged In')
        else:
            return HttpResponse('Wrong Credentials')

    return render(request, 'login.html')
