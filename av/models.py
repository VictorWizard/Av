from django.db import models
from django.contrib.auth import get_user_model
import datetime

class Calculate_price(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    type = models.ForeignKey('Types_of_car', on_delete=models.PROTECT, null=True, verbose_name='Тип автомобиля')
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
    type = models.ForeignKey('Types_of_car', on_delete=models.PROTECT, null=True, verbose_name='Тип автомобиля')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')
    price = models.CharField(max_length=200, verbose_name='Цена')
    class Meta:
        verbose_name_plural = 'Услуги+цена'
        verbose_name = 'Услуги+цена'
        ordering = ['service']
        
class Tel_number(models.Model):
    tel_number = models.CharField(max_length=50, db_index=True, verbose_name='Номер телефона')
    def __str__(self):
        return self.tel_number
    class Meta:
        verbose_name_plural = 'Номер телефона'
        verbose_name = 'Номер телефона'

class Address(models.Model):
    address = models.CharField(max_length=100, db_index=True, verbose_name='Адрес')
    def __str__(self):
        return self.address
    class Meta:
        verbose_name_plural = 'Адрес'
        verbose_name = 'Адрес'

class Appointments(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    tel = models.CharField(max_length=200, db_index=True, verbose_name='Номер телефона')
    e_mail = models.CharField(max_length=200, blank=True, db_index=True, verbose_name='Номер телефона')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    type = models.ForeignKey('Types_of_car', on_delete=models.PROTECT, null=True, verbose_name='Тип автомобиля')
    date_created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации заявки')
    date_service = models.DateField(db_index=True, verbose_name='Дата')
    time_service = models.TimeField(db_index=True, verbose_name='Время')
    price = models.CharField(max_length=50, db_index=True, null=True, verbose_name='Цена')
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        price = ''
        if self.name != None:
            for i in Services_prices.objects.all():
                ccar = i.car
                sservice = i.service
                ttype = i.type
                if self.car == ccar and self.service == sservice and self.type == ttype:
                    self.price = i.price
                    break
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Записи на мойку'
        verbose_name = 'Записи на мойку'
        ordering = ['date_created']

class Feedbacks(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    e_mail = models.CharField(max_length=200, blank=True, db_index=True, verbose_name='Номер телефона')
    rating = models.CharField(max_length=1, db_index=True, verbose_name='Оценка по 10-бальной шкале')
    feedback = models.CharField(max_length=200, db_index=True, verbose_name='Отзыв')
    date_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации отзыва')
    class Meta:
        verbose_name_plural = 'Отзывы об автомойке'
        verbose_name = 'Отзывы об автомойке'
        ordering = ['date_published']