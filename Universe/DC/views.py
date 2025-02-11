from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Batman(response):
    return HttpResponse('<h1> I am Batman </h1>')

def WonderWomen(response):
    return HttpResponse('<h1> I am WonderWomen</h1>')