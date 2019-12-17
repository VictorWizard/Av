from .models import Tel_number

def tel_number(request):
    return {"tel_number": Tel_number.objects.first()}