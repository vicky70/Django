from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> This is a Home page </h1>')

def about(request):
    return HttpResponse('<h1> This is a About page </h1>')

def contact(request):
    return HttpResponse('<h1> This is a Contact page </h1>')