from django.shortcuts import render
from django.http import Http404


def adminPage(request):
    raise Http404("You're not allowed here!!!")


def index(request):
    return render(request, 'shop/index.html')
