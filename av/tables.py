import django_tables2 as tables
from .models import Services_prices, Services, Cars
from django.utils.html import format_html
from django.db.models.functions import Length

class ServicesTable(tables.Table):
    class Meta:
        model = Services_prices
        template_name = "django_tables2/bootstrap.html"
        fields = ("car", "service", "price")