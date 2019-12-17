from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('av.urls')),
    path('admin/', admin.site.urls),
]