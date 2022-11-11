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

class Ingredient(models.Model):
    name = models.CharField(max_length = 200, null = True, blank = True)
    amount = models.CharField(max_length = 200, null = True, blank = True)

    
    def __str__(self):
        return self.name
class Location(models.Model):
    location = models.CharField(max_length = 20)

    def __str__(self):
        return self.location

class Menu_Item(models.Model):
    title = models.CharField(max_length = 200, null = True, name = 'title')
    description = models.CharField(max_length = 600, null = True)
    price = models.FloatField(null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    location = models.ManyToManyField(Location)
    
    def json(self):
        location = [i.id for i in Menu_Item.objects.get(pk=self.id).location.all()]
        return {
        'title': self.title,
        'description': self.description,
        'price': self.price,
        'location': location,
        'cuisine': {
            'title': self.cuisine.cuisine_name,
        },
        'category': { 
            'title': self.category.category_name },
        'ingredients':  [{"name": i.name, "amount": i.amount, } for i in Menu_Item.objects.get(pk=self.id).ingredients.all() ],
        }


    def __str__(self):
        return self.description

    
