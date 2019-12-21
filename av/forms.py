from django import forms
from .models import Calculate_price, Services, Cars, Services_prices, Appointments

class CarsForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), label='Модель автомобиля', required = False, widget=forms.widgets.Select())
    service = forms.ModelChoiceField(queryset=Services.objects.all(), label='Тип услуги', required = False, widget=forms.widgets.Select())
    class Meta:
        model = Calculate_price
        fields = ('car', 'type', 'service')
        
class AppointmentForm(forms.ModelForm):
    date_service = forms.DateTimeField(widget=forms.widgets.SelectDateWidget)
    class Meta:
        model = Appointments
        fields = ('name', 'tel', 'e_mail', 'service', 'car', 'type', 'date_service')