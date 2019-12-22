from .models import Tel_number, Address

def tel_number(request):
    return {"tel_number": Tel_number.objects.first()}

def address(request):
    return {"address": Address.objects.first()}