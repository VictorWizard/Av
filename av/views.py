from django.shortcuts import render
from .forms import CarsForm
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number
from .tables import ServicesTable

def index(request):
    content = 'Тут будет содержимое'
    context = {'content': content,}
    return render(request, 'av/index.html', context)
    
def calculate(request):
    pprice = ''
    if request.method == 'GET':
        form = CarsForm(request.GET)
        if form.is_valid():
            car = form.cleaned_data.get("car")
            service = form.cleaned_data.get("service")   
            for i in Services_prices.objects.all():
                ccar = i.car
                sservice = i.service
                if car == ccar and service == sservice:
                    pprice = i.price
                    break
                elif (car == None and service != None) or (car != None and service == None):
                    pprice = 'Заполните все поля для получения цены за услугу'
                elif car == None and service == None:
                    pprice = ''
                else:
                    pprice = 'Нет такой услуги для выбранного автомобиля'
            if pprice == '':
                pprice = ''
    context = {'form': form, 'price': pprice}
    return render(request, 'av/calculate.html', context)
    
def prices(request):
    queryset = Services_prices.objects.all()
    table = ServicesTable(queryset)
    return render(request, "av/prices.html", {
        "table": table
    })
    
def about(request):
    content = 'Информация об автомойке'
    context = {'content': content}
    return render(request, 'av/about.html', context)