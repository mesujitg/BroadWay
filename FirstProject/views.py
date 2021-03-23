from django.http import HttpResponse
from django.shortcuts import render


def show_home(request):
    return render(request, 'index.html')


def show_portfolio(request):
    return render(request, 'portfolio.html')
