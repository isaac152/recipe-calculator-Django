# Generated by Django 3.2.7 on 2021-10-15 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_remove_recipe_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='profile',
        ),
    ]