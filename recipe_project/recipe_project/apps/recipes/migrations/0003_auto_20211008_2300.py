# Generated by Django 3.2.7 on 2021-10-08 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20211008_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingprice',
            name='ingredient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingprice',
            name='measure',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes.measure'),
        ),
        migrations.AlterField(
            model_name='ingprice',
            name='quantity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes.quantity'),
        ),
    ]
