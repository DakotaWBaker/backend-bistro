from django.db import models

# Create your models here.

class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cuisine_name

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Menu_Item(models.Model):
    title = models.CharField(max_length = 200, null = True, name = 'title')
    description = models.CharField(max_length = 600, null = True)
    price = models.FloatField(null=True)
    cuisine_id = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def json(self):
        return {
        'title': self.title,
        'description': self.description,
        'price': self.price,
        'cuisine': {
            'title': self.cuisine_id.cuisine_name,
        },
        'category': { 
            'title': self.category_id.category_name }


       
        }
#         people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# print(people)
    def __str__(self):
        return self.description
#     Menu Items
# Title
# Description
# Price
# Spicy Level
# FK to Category
# FK to Cuisine
# Category (Appetizer, Dessert, Main Dish, etc.)
# Cuisine (American, Thai, etc.)

