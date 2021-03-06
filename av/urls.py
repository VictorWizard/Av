from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageCreateView.as_view(), name='index'),
    #path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('prices/', views.prices, name='prices'),
    path('appointment/', views.AppointmentCreateView.as_view(), name='appointment'),
    path('success/', views.success, name='success'),
]