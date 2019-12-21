from django.db import models
from django.contrib.auth import get_user_model
import datetime

class Calculate_price(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    type = models.ForeignKey(Types_of_car, on_delete=models.PROTECT, verbose_name='Тип автомобиля')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')
    class Meta:
        verbose_name_plural = 'Расчет стоимости'
        verbose_name = 'Расчет стоимости'
    
class Cars(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Модель автомобиля')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Модели автомобилей'
        verbose_name = 'Модель автомобиля'
        ordering = ['name']

class Types_of_car(models.Model):
    type = models.CharField(max_length=200, db_index=True, verbose_name='Тип автомобиля')
    def __str__(self):
        return self.type
    class Meta:
        verbose_name_plural = 'Типы автомобилей'
        verbose_name = 'Типы автомобиля'
        ordering = ['type']
        
class Services(models.Model):
    service = models.CharField(max_length=200, db_index=True, verbose_name='Тип услуги')
    def __str__(self):
        return self.service
    class Meta:
        verbose_name_plural = 'Виды услуг'
        verbose_name = 'Виды услуг'
        
class Services_prices(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    type = models.ForeignKey('Types_of_car', on_delete=models.PROTECT, verbose_name='Тип автомобиля')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')
    price = models.CharField(max_length=200, verbose_name='Цена')
    class Meta:
        verbose_name_plural = 'Услуги+цена'
        verbose_name = 'Услуги+цена'
        ordering = ['service']
        
class Tel_number(models.Model):
    tel_number = models.CharField(max_length=30, db_index=True, verbose_name='Номер телефона')
    def __str__(self):
        return self.tel_number
    class Meta:
        verbose_name_plural = 'Номер телефона'
        verbose_name = 'Номер телефона'

class Appointments(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    tel = models.CharField(max_length=200, db_index=True, verbose_name='Номер телефона')
    e_mail = models.CharField(max_length=200, blank=True, db_index=True, verbose_name='Номер телефона')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    type = models.ForeignKey('Types_of_car', on_delete=models.PROTECT, verbose_name='Тип автомобиля')
    date_created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации заявки')
    date_service = models.DateTimeField(db_index=True, verbose_name='Дата')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Записи на мойку'
        verbose_name = 'Записи на мойку'
        ordering = ['date_created']