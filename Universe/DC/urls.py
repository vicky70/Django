from django.urls import path
from . import views

urlpatterns = [
    path('Batman/', views.Batman),
    path('WonderWomen/', views.WonderWomen)
]