#General import
from django.shortcuts import redirect
#View import 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from .forms import RecipeForm,IngredientCreationFormSet
#url
from django.urls import reverse_lazy
#Models
from . models import IngPrice,Ingredient,Quantity,Recipe



class Home(LoginRequiredMixin,TemplateView):
    template_name='users/home.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)


class CreateRecipe(LoginRequiredMixin,TemplateView):
    template_name='recipes/recipe.html'

    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST,extra=request.POST.get('extra_category_count'))
        if form.is_valid():
            form_cleaned = form.cleaned_data
            ingredients = self.list_ingredients(form_cleaned)
            price = sum([i.price for i in ingredients])
            recipe=Recipe.objects.create(
                name=form_cleaned['name'],
                description = form_cleaned['description'],
                user = self.request.user.profile,
                category = form_cleaned['category'],
                price= price
            )
            recipe.save()
            [i.recipes.add(recipe) for i in ingredients]
        return redirect(reverse_lazy('recipes:create'))
    
    def list_ingredients(self,form):
        ingredients = [form['ingredients']]
        for i in range(int(form['extra_category_count'])):
            ingredients.append(form[f'extra_category_{i}'])
        return ingredients


"""

    name= models.TextField(verbose_name="Name",null=False)
    description= models.TextField(verbose_name="Description")
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False)
    image = models.ImageField(upload_to='recipe/', blank=True, null=True)
    price= models.DecimalField(default=0.00,max_digits=9,decimal_places=2,verbose_name="Price",null=False)
"""


class CreateIngredient(LoginRequiredMixin,TemplateView):
    template_name='recipes/ingredient.html'

    def get(self, request, *args, **kwargs):
        formset=IngredientCreationFormSet(request.GET or None)
        return self.render_to_response({'ingredient_formset': formset})


    def post(self, *args, **kwargs):
        formset = IngredientCreationFormSet(data=self.request.POST)
        if formset.is_valid():
            for form in formset:
                form_cleaned = form.cleaned_data
                measure_form=form_cleaned['measure']
                ingredient_form=self.check_if_exist_object(Ingredient,{'name':form_cleaned['name']})
                quantity_form=self.check_if_exist_object(Quantity,{'amount':form_cleaned['quantity']})
                IngPrice.objects.create(
                    measure=measure_form,
                    ingredient=ingredient_form,
                    quantity=quantity_form,
                    price=form_cleaned['price']
                    ).save()
            return redirect(reverse_lazy('recipes:create'))
        else:
            return self.render_to_response({'ingredient_formset': formset})

    def check_if_exist_object(self,model,filter):
        obj,created = model.objects.get_or_create(**filter)
        return obj
            
        