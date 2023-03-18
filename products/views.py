from django.shortcuts import render
from .models import Products


# Create your views here.

def product(request):
    context = {
        'Products':Products.objects.all()
    }
    print(context)
    return render (request, 'index.html' , context)
