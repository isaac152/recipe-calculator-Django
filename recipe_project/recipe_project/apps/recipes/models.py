from django.db import models

class Category(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

class Recipe(models.Model):
    name= models.TextField(verbose_name="Name",null=False)
    description= models.TextField(verbose_name="Description")
    #user_id
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    image = models.ImageField(upload_to='recipe/', blank=True, null=True)
    price= models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Price",null=False)
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['id']    


class Ingredient(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ['id']

class Measure(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Measure'
        verbose_name_plural = 'Measures'
        ordering = ['id']

class Quantity(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        ordering = ['id']

class IngPrice(models.Model):
    recipes = models.ManyToManyField(Recipe)
    price= models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Price",null=False)
    ingredient=models.ForeignKey(Ingredient,on_delete=models.CASCADE,null=False)
    measure=models.ForeignKey(Measure,on_delete=models.CASCADE,null=False)
    quantity=models.ForeignKey(Quantity,on_delete=models.CASCADE,null=False)
    class Meta:
        verbose_name = 'Ingredient price'
        verbose_name_plural = 'Ingredient prices'
        ordering = ['id']
