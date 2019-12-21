from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CarsForm, AppointmentForm
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number, Appointments, Types_of_car
from .tables import ServicesTable

def index(request):
    content = 'Тут будет содержимое'
    services = Services.objects.all()
    context = {'content': content, 'services': services}
    return render(request, 'av/index.html', context)

class AppointmentCreateView(CreateView):
    template_name = 'av/appointment.html'
    form_class = AppointmentForm
    success_url = '/appointment'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointment'] = Appointments.objects.all()
        return context
    
def calculate(request):
    pprice = ''
    if request.method == 'GET':
        form = CarsForm(request.GET)
        if form.is_valid():
            car = form.cleaned_data.get("car")
            service = form.cleaned_data.get("service")
            type = form.cleaned_data.get("type")
            for i in Services_prices.objects.all():
                ccar = i.car
                sservice = i.service
                ttype = i.type
                if car == ccar and service == sservice and type == ttype:
                    pprice = i.price
                    break
                elif car == None and service == None and type == None:
                    pprice = ''
                else:
                    pprice = 'Нет такой услуги для выбранного автомобиля'
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