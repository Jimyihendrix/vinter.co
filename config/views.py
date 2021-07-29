from django.shortcuts import render # <-??

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>vinter.co - Vinter Capital, building the free economy</h1>")