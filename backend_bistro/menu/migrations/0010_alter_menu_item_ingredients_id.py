# Generated by Django 4.1.3 on 2022-11-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_remove_ingredient_menu_id_menu_item_ingredients_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='ingredients_id',
            field=models.ManyToManyField(related_name='menuitems', to='menu.ingredient'),
        ),
    ]
