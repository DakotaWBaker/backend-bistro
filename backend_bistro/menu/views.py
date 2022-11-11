from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Menu_Item, Location, Ingredient
from django.core import serializers
from django.forms.models import model_to_dict
import csv

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def full_menu(request):
    data = [i.json() for i in Menu_Item.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")

def ctv_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="HappyGrillmore.csv"',  
    writer = csv.writer(response)
    menu_items = Menu_Item.objects.all()
    location = Location.objects.all()
    
    row = writer.writerow(['Item Name', 'Description', 'Price', 'Category', 'Cuisine'])
    
    for menu in menu_items:
            writer.writerow([menu.title, menu.description, menu.price, menu.category.category_name, menu.cuisine.cuisine_name])
    
    return response
