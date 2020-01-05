from django.db import models


class Calculate_price(models.Model):
    car = models.ForeignKey('Cars', on_delete=models.PROTECT, verbose_name='Модель автомобиля')
    service = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Тип услуги')

    class Meta:
        verbose_name_plural = 'Расчет стоимости'
        verbose_name = 'Расчет стоимости'


class Cars(models.Model):
    car = models.CharField(max_length=200, null=True, db_index=True, verbose_name='Тип автомобиля')

    def __str__(self):
        return self.car

    class Meta:
        verbose_name_plural = 'Типы автомобилей'
        verbose_name = 'Тип автомобиля'
        ordering = ['car']


class Services(models.Model):
    service = models.CharField(max_length=200, null=True, db_index=True, verbose_name='Тип услуги')

    def __str__(self):
        return self.service

    class Meta:
        verbose_name_plural = 'Виды услуг'
        verbose_name = 'Виды услуг'


class Services_prices(models.Model):
    car = models.ForeignKey('Cars', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Тип автомобиля')
    service = models.ForeignKey('Services', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Тип услуги')
    price = models.CharField(max_length=200, null=True, blank=True, verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Услуги+цена'
        verbose_name = 'Услуги+цена'
        ordering = ['-car']


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


class Clients(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    num_car = models.CharField(max_length=200, null=True, db_index=True, verbose_name='Гос.номер автомобиля')
    count = models.IntegerField(default=0, db_index=True, verbose_name='Количество моек')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиенты'
        ordering = ['count']


class Appointments(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    tel = models.CharField(max_length=200, db_index=True, verbose_name='Номер телефона')
    e_mail = models.CharField(max_length=200, blank=True, db_index=True, verbose_name='E-mail')
    car = models.ForeignKey('Cars', null=True, on_delete=models.PROTECT, verbose_name='Тип автомобиля')
    num_car = models.CharField(max_length=200, null=True, db_index=True, verbose_name='Гос.номер автомобиля')
    service1 = models.ForeignKey(Services, null=True, blank=True, on_delete=models.PROTECT, related_name='first_service', verbose_name='Тип услуги')
    service2 = models.ForeignKey(Services, null=True, blank=True, on_delete=models.PROTECT, related_name='second_service',  verbose_name='Тип услуги(опционально)')
    service3 = models.ForeignKey(Services, null=True, blank=True, on_delete=models.PROTECT, related_name='three_service',  verbose_name='Тип услуги(опционально)')
    date_created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации заявки')
    date_service = models.DateField(db_index=True, verbose_name='Дата')
    time_service = models.TimeField(db_index=True, verbose_name='Время')
    price = models.CharField(max_length=200, db_index=True, null=True, verbose_name='Цена')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        counter = 0
        if self.name != None:
            if Clients.objects.count() != 0:
                for n in Clients.objects.all():
                    if n.name == self.name or n.num_car == self.name:
                        if n.count == 0:
                            n.count = 1
                            if n.num_car == self.num_car:
                                n.save()
                            else:
                                n.num_car = n.num_car + ', ' + self.num_car
                                n.save()
                        elif n.count == 1:
                            n.count = 2
                            if n.num_car == self.num_car:
                                n.save()
                            else:
                                n.num_car = n.num_car + ', ' + self.num_car
                                n.save()
                        elif n.count == 2:
                            n.count = 3
                            if n.num_car == self.num_car:
                                n.save()
                            else:
                                n.num_car = n.num_car + ', ' + self.num_car
                                n.save()
                        elif n.count == 3:
                            n.count = 4
                            if n.num_car == self.num_car:
                                n.save()
                            else:
                                n.num_car = n.num_car + ', ' + self.num_car
                                n.save()
                        elif n.count == 4:
                            n.count = 5
                            if n.num_car == self.num_car:
                                n.save()
                            else:
                                n.num_car = n.num_car + ', ' + self.num_car
                                n.save()
                        elif n.count == 5:
                            n.count = 1
                            n.num_car = self.num_car
                            n.save()
                        counter = n.count
                    else:
                        Clients.objects.create(name=self.name, num_car=self.num_car, count=1)
            else:
                Clients.objects.create(name=self.name, num_car=self.num_car, count=1)
            if counter == 5:
                self.price = 'Бесплатно(5-ая мойка)'
            else:
                for i in Services_prices.objects.all():
                    ccar = i.car
                    sservice = i.service
                    a = "Мойка двигателя"
                    b = "Стирка ковров"
                    c = "Химчистка"
                    if (self.car == ccar and self.service1 == sservice) or (ccar == None and self.service1 == sservice):
                        if self.service1 != None and self.service2 == None and self.service3 == None:
                            self.price = i.price
                            break
                        elif self.service1 != None and self.service2 != None and self.service3 == None:
                            if str(self.service1) != a and str(self.service1) != b and str(self.service1) != c:
                                self.price = int(i.price)
                                print(self.price)
                                print(i.price)
                                print(type(self.service1))
                            elif str(self.service1) == a:
                                self.price = 1500
                            elif str(self.service1) == b:
                                self.price = 250
                            elif str(self.service1) == c:
                                self.price = 25000
                            else:
                                self.price = 2000000
                            for d in Services_prices.objects.all():
                                if (self.car == d.car and self.service2 == d.service) or (d.car == None and self.service2 == d.service):
                                    if str(self.service2) != a and str(self.service2) != b and str(self.service2) != c:
                                        self.price += int(d.price)
                                    elif str(self.service2) == a:
                                        self.price += 1500
                                    elif str(self.service2) == b:
                                        self.price += 250
                                    elif str(self.service2) == c:
                                        self.price += 25000
                                    break
                        elif self.service1 != None and self.service2 != None and self.service3 != None:
                            if str(self.service1) != a and str(self.service1) != b and str(self.service1) != c:
                                self.price = int(i.price)
                            elif str(self.service1) == a:
                                self.price = 1500
                            elif str(self.service1) == b:
                                self.price = 250
                            elif str(self.service1) == c:
                                self.price = 25000
                            for d in Services_prices.objects.all():
                                if (self.car == d.car and self.service2 == d.service) or (d.car == None and self.service2 == d.service):
                                    if str(self.service2) != a and str(self.service2) != b and str(self.service2) != c:
                                        self.price += int(d.price)
                                    elif str(self.service2) == a:
                                        self.price += 1500
                                    elif str(self.service2) == b:
                                        self.price += 250
                                    elif str(self.service2) == c:
                                        self.price += 25000
                                    for e in Services_prices.objects.all():
                                        if (self.car == e.car and self.service3 == e.service) or (e.car == None and self.service3 == e.service):
                                            if str(self.service3) != a and str(self.service3) != b and str(self.service3) != c:
                                                self.price += int(e.price)
                                            elif str(self.service3) == a:
                                                self.price += 1500
                                            elif str(self.service3) == b:
                                                self.price += 250
                                            elif str(self.service3) == c:
                                                self.price += 25000
                                            break
                        else:
                            self.price = 'Не удалось рассчитать стоимость1'
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Записи на мойку'
        verbose_name = 'Записи на мойку'
        ordering = ['-date_created']


class Feedbacks(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя, фамилия')
    e_mail = models.CharField(max_length=200, blank=True, db_index=True, verbose_name='Номер телефона')
    rating = models.CharField(max_length=1, db_index=True, verbose_name='Оценка по 5-бальной шкале')
    feedback = models.TextField(max_length=200, db_index=True, verbose_name='Отзыв')
    date_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации отзыва')

    class Meta:
        verbose_name_plural = 'Отзывы об автомойке'
        verbose_name = 'Отзывы об автомойке'
        ordering = ['date_published']