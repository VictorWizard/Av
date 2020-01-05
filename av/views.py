from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import FeedbackForm, CarsForm, AppointmentForm
from .models import Services_prices, Services, Appointments
from .tables import ServicesTable


class MainPageCreateView(CreateView):
    template_name = 'av/index.html'
    form_class = FeedbackForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content'] = 'Автомойка «У ГАИ»'
        context['services'] = Services.objects.all()
        return context

class AppointmentCreateView(CreateView):
    template_name = 'av/appointment.html'
    form_class = AppointmentForm
    success_url = '/success'
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
            for i in Services_prices.objects.all():
                ccar = i.car
                sservice = i.service
                if car == ccar and service == sservice:
                    pprice = i.price
                    break
                elif car == None and service == None:
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

def success(request):
    price_from_success = Appointments.objects.last().price
    context = {'price_from_success': price_from_success}
    return render(request, 'av/success.html', context)