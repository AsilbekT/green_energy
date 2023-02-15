from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "index.html", context)


def product(request):
    products = Product.objects.all()

    context = {"products": products}
    return render(request, "project_2.html", context)
