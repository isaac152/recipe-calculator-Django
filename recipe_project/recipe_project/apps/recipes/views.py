#General import
from django.shortcuts import redirect
#View import 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from .forms import RecipeForm,IngredientForm
#Models
from . models import IngPrice,Ingredient,Quantity


class Home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:index')
        return super().dispatch(request, *args, **kwargs)


class CreateRecipe(LoginRequiredMixin,FormView):
    template_name='recipes/recipe.html'
    form_class=RecipeForm


class CreateIngredient(LoginRequiredMixin,FormView):
    template_name='recipes/ingredient.html'
    form_class=IngredientForm
    success_url="."

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
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
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def check_if_exist_object(self,model,filter):
        if(not model.objects.get(**filter)):
            check_model=model.objects.create(**filter).save()
        else:
            check_model=model.objects.get(**filter)
        return check_model