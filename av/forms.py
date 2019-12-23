from django import forms
from .models import Calculate_price, Services, Cars, Services_prices, Appointments, Feedbacks
from django.contrib.admin import widgets

class CarsForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), label='Модель автомобиля', required = False, widget=forms.widgets.Select())
    service = forms.ModelChoiceField(queryset=Services.objects.all(), label='Тип услуги', required = False, widget=forms.widgets.Select())
    class Meta:
        model = Calculate_price
        fields = ('car', 'type', 'service')

class AppointmentForm(forms.ModelForm):
    date_service = forms.DateField(help_text='Введите дату в таком формате: 12.12.2019', widget=forms.widgets.DateInput)
    time_service = forms.TimeField(widget=forms.widgets.TimeInput, help_text="Введите время в таком формате: 15:00")
    class Meta:
        model = Appointments
        fields = ('name', 'tel', 'e_mail', 'service', 'car', 'type', 'date_service', 'time_service')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ('name', 'e_mail', 'rating', 'feedback')
        widgets = {
            'feedback': forms.Textarea(attrs={'rows':4, 'cols':48}),
        }