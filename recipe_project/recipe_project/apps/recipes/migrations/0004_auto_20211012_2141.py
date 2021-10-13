# Generated by Django 3.2.7 on 2021-10-12 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20211008_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingprice',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingprice',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.measure'),
        ),
        migrations.AlterField(
            model_name='ingprice',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.quantity'),
        ),
    ]
