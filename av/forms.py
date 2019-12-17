from django import forms
from .models import Calculate_price, Services, Cars, Services_prices

class CarsForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), label='Модель автомобиля', required = False, widget=forms.widgets.Select())
    service = forms.ModelChoiceField(queryset=Services.objects.all(), label='Тип услуги', required = False, widget=forms.widgets.Select())
    # if form.is_valid():
        # firstname= form.cleaned_data.get("first_name")
        # lastname= form.cleaned_data.get("last_name")
    # for i in Services_prices.objects.all():
        # sservice = i.service
        # if sservice == 
    # lol = Services.objects.get(service=i)
    class Meta:
        model = Calculate_price
        fields = ('car', 'service')
        
# from django import forms

# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# import datetime #for checking renewal date range.
    
# class RenewBookForm(forms.Form):
    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    # def clean_renewal_date(self):
        # data = self.cleaned_data['renewal_date']
        
        # #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом). 
        # if data < datetime.date.today():
            # raise ValidationError(_('Invalid date - renewal in past'))

        # #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        # if data > datetime.date.today() + datetime.timedelta(weeks=4):
            # raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # # Помните, что всегда надо возвращать "очищенные" данные.
        # return data