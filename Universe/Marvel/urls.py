from django.urls import path
from . import views

urlpatterns = [
    path('Ironman/', views.Ironman),
    path('Hulk/', views.Hulk)
]