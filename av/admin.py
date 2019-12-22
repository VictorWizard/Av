from django.contrib import admin
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number, Appointments, Types_of_car, Feedbacks, Address

class AvAdmin(admin.ModelAdmin):
    list_display = ('service', 'car', 'price')
    list_display_links = ('service', 'car', 'price')
    search_fields = ('service', 'car', 'price')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_service')
    list_display_links = ('name', 'date_created', 'date_service')
    search_fields = ('name', 'date_created', 'date_service')
    readonly_fields = ['date_created']

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_mail', 'rating', 'feedback')
    list_display_links = ('name', 'e_mail', 'rating', 'feedback')
    search_fields = ('name', 'e_mail', 'rating', 'feedback')

admin.site.register(Appointments, AppointmentAdmin)
admin.site.register(Calculate_price)
admin.site.register(Cars)
admin.site.register(Services_prices, AvAdmin)
admin.site.register(Services)
admin.site.register(Tel_number)
admin.site.register(Address)
admin.site.register(Types_of_car)
admin.site.register(Feedbacks, FeedbacksAdmin)