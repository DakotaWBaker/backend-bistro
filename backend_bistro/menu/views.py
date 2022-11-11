from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Menu_Item, Location, Ingredient
from django.core import serializers
from django.forms.models import model_to_dict
import csv
from django.views.decorators.http import require_http_methods


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#View for returning json object
@require_http_methods(["GET"]) #Decorator only allowing get requests
def full_menu(request):
    try:
        data = [i.json() for i in Menu_Item.objects.all()]      #Calling json method on Menu_Item and looping through
        return HttpResponse(json.dumps(data), content_type="application/json")  #Returning http response. json.dumps parses to jason
        #Checking if Menu_item model does not exist and raises error if true
    except Menu_Item.DoesNotExist:
        errmsg = "Does not exist"
        raise err(errmsg)

#View for making .csv file
@require_http_methods(["GET"]) #Decorator only allowing get requests
def csv_view(request):
    try:
        response = HttpResponse(content_type="text/csv") #Http response setting content type to csv file
        response["Content-Disposition"] = ('attachment; filename="HappyGrillmore.csv"',)    #Content-Disposition that describes how to process and sets it to an attachment defining filename
        writer = csv.writer(response)       #Setting csv writer to writes
        menu_items = Menu_Item.objects.all()
        location = Location.objects.all()
        
        #Writer.writerow to write row of csv file. Initial column names
        row = writer.writerow(
            ["Item Name", "Description", "Price", "Category", "Cuisine"]
        )

        #Looping through menu_items objects setting each field to a column
        for menu in menu_items:
            writer.writerow(
                [
                    menu.title,
                    menu.description,
                    menu.price,
                    menu.category.category_name,
                    menu.cuisine.cuisine_name,
                ]
            )

        return response
    except Menu_Item.DoesNotExist:
        errmsg = "Does not exist"
        raise err(errmsg)
