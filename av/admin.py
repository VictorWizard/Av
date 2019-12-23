from django.contrib import admin
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number, Appointments, Types_of_car, Feedbacks, Address, Clients

class AvAdmin(admin.ModelAdmin):
    list_display = ('service', 'car', 'price')
    list_display_links = ('service', 'car', 'price')
    search_fields = ('service', 'car', 'price')

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_service', 'time_service', 'date_created')
    list_display_links = ('name', 'date_service', 'time_service', 'date_created')
    search_fields = ('name', 'date_service', 'time_service', 'date_created')
    readonly_fields = ['date_created']

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')
    list_display_links = ('name', 'count')
    search_fields = ('name', 'count')

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_mail', 'rating', 'feedback')
    list_display_links = ('name', 'e_mail', 'rating', 'feedback')
    search_fields = ('name', 'e_mail', 'rating', 'feedback')

admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(Calculate_price)
admin.site.register(Cars)
admin.site.register(Services_prices, AvAdmin)
admin.site.register(Services)
admin.site.register(Tel_number)
admin.site.register(Address)
admin.site.register(Types_of_car)
admin.site.register(Feedbacks, FeedbacksAdmin)
admin.site.register(Clients, ClientsAdmin)