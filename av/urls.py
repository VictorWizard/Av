from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('prices/', views.prices, name='prices'),
    path('about/', views.about, name='about'),
]