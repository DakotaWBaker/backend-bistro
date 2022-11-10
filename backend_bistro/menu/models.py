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
    name = models.CharField(max_length = 200)

    
    def __str__(self):
        return self.name
        

class Menu_Item(models.Model):
    title = models.CharField(max_length = 200, null = True, name = 'title')
    description = models.CharField(max_length = 600, null = True)
    price = models.FloatField(null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def json(self):
        return {
        'title': self.title,
        'description': self.description,
        'price': self.price,
        'cuisine': {
            'title': self.cuisine.cuisine_name,
        },
        'category': { 
            'title': self.category.category_name },
        # 'ingredients': [ {"name": i.name, "amt": '10 cups' } for i in Menu_Item.objects.get(pk=self.id).ingredients.all() ],
        'ingredients':  [{"name": i.name, "amt": '10 cups' } for i in Menu_Item.objects.get(pk=self.id).ingredients.all() ],
        }


    def __str__(self):
        return self.description

# class ModelIngredient(models.Model):
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     menu_item = models.ForeignKey(Menu_Item, on_delete=models.CASCADE)
#     name = models.CharField(max_length = 200)
    
