from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Ironman():
    return HttpResponse('<h>I am Ironman</h>')

def Hulk():
    return HttpResponse('<h1> I am Hulk')
