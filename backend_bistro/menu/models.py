from django.db import models



#Model for Cuisine types
class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=200)

    def __str__(self):
        return self.cuisine_name

#Model for Category Types
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

#Model for Ingredients
class Ingredient(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

#Model for Restaurant location
class Location(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location

#Main Menu_items Model
class Menu_Item(models.Model):
    title = models.CharField(max_length=200, null=True, name="title")
    description = models.CharField(max_length=600, null=True)
    price = models.FloatField(null=True)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE)    #Foreign key referencing cuisine types. 1 to many
    category = models.ForeignKey("Category", on_delete=models.CASCADE)  #Foreign key referencing category types. 1 to many
    ingredients = models.ManyToManyField(Ingredient)        #Many to many field referencing ingredient model
    location = models.ManyToManyField(Location)             #Many to many field referencing restaurant location

    #Class method for Serializing json data and creating a boiler plate to outline api format initially used in react restaurant so I dont have to change react code
    def json(self):
        location = [i.id for i in Menu_Item.objects.get(pk=self.id).location.all()]
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "location": location,
            "cuisine": {
                "title": self.cuisine.cuisine_name,
            },
            "category": {"title": self.category.category_name},
            "ingredients": [
                {
                    "name": i.name,
                    "amount": i.amount,
                }
                for i in Menu_Item.objects.get(pk=self.id).ingredients.all()
            ],
        }

    def __str__(self):
        return self.description
