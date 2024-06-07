from django.shortcuts import render
from .models import Product

def Home(request):
    return render(request ,'home.html')

