from django.contrib import admin
from .models import Calculate_price, Cars, Services_prices, Services, Tel_number

class AvAdmin(admin.ModelAdmin):
    list_display = ('service', 'car', 'price')
    list_display_links = ('service', 'car', 'price')
    search_fields = ('service', 'car', 'price')

admin.site.register(Calculate_price)
admin.site.register(Cars)
admin.site.register(Services_prices, AvAdmin)
admin.site.register(Services)
admin.site.register(Tel_number)