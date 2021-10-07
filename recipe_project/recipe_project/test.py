from .apps.recipes.models import Measure,Category

category_recipes = ['Breakfast','Fish','Lunch','Main','Pasta','Salad','Desserts','Drinks','Snack']
measure_recipes =  ['kg','gr','mL','l','cup','oz','gal','lb','tbsp']


for i in category_recipes:
    category=Category.objects.create(name=i).save()

for i in measure_recipes:
    measure=Measure.objects.create(name=i).save()
