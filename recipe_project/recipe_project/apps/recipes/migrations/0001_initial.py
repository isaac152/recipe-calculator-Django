# Generated by Django 3.2.7 on 2021-10-01 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Quantity',
                'verbose_name_plural': 'Quantities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe/')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.category')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IngPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Price')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.measure')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.quantity')),
                ('recipes', models.ManyToManyField(to='recipes.Recipe')),
            ],
            options={
                'verbose_name': 'Ingredient price',
                'verbose_name_plural': 'Ingredient prices',
                'ordering': ['id'],
            },
        ),
    ]