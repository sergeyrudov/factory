from django.shortcuts import render
from .models import Category, Factory, Product
from django.http import HttpResponse

# Create your views here.

def allcategories(request):
    factory = Factory.objects.all()
    context = {'categories': factory}
    return render(request, 'factory/allcategories.html', context)

def category(request,id):
    cat = Category.objects.get(id=id)
    context = {'category' : cat}
    return render(request, 'factory/category.html', context)