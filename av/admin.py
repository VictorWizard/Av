from django.contrib import admin
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number, Appointments, Feedbacks, Address, Clients

class AvAdmin(admin.ModelAdmin):
    list_display = ('car', 'service', 'price')
    list_display_links = ('car', 'service', 'price')
    search_fields = ('car', 'service', 'price')

class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_service', 'time_service', 'service', 'price')
    list_display_links = ('name', 'date_service', 'time_service')
    search_fields = ('name', 'date_service', 'time_service')
    readonly_fields = ['date_created']

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_car', 'count')
    list_display_links = ('name', 'num_car')
    search_fields = ('name', 'num_car')

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
admin.site.register(Feedbacks, FeedbacksAdmin)
admin.site.register(Clients, ClientsAdmin)