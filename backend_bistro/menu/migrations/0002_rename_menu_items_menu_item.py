# Generated by Django 4.1.3 on 2022-11-09 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu_Items',
            new_name='Menu_Item',
        ),
    ]
