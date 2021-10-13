from django.db import models
from ..users.models import Profile

class Category(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']
    def __str__(self) -> str:
        return f" {self.name}"


class Recipe(models.Model):
    name= models.TextField(verbose_name="Name",null=False)
    description= models.TextField(verbose_name="Description")
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
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
    def __str__(self) -> str:
        return f" {self.name}"

class Measure(models.Model):
    name= models.TextField(verbose_name="Name",null=False,unique=True)

    class Meta:
        verbose_name = 'Measure'
        verbose_name_plural = 'Measures'
        ordering = ['id']

    def __str__(self) -> str:
        return f" {self.name}"

class Quantity(models.Model):
    amount= models.PositiveIntegerField(verbose_name="amount",null=False,unique=True)

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        ordering = ['id']
    
    def __str__(self) -> str:
        return f" {self.amount}"

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

    def __str__(self):
        return f"{self.ingredient} {self.quantity} {self.measure} Price: {self.price}"