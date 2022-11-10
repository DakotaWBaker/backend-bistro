from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Menu_Item
from django.core import serializers
from django.forms.models import model_to_dict

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def full_menu(request):
    data = [i.json() for i in Menu_Item.objects.all()]
    return HttpResponse(json.dumps(data), content_type="application/json")
