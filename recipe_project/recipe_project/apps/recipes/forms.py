from django import forms
from django.forms import formset_factory

from .models import Category,Measure,IngPrice


class RecipeForm(forms.Form):
    name = forms.CharField(
        label="Recipe name",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Enter Recipe name"
            }
        )
    )
    descriptio = forms.CharField(
        label="Recipe description",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Enter recipe description"
            }
        )
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,to_field_name='name')

    ingredientes = forms.ModelChoiceField(queryset=IngPrice.objects.all(),required=True)

    def __init__(self,*args, **kwargs):
        super(RecipeForm,self).__init__(*args, **kwargs)



class IngredientForm(forms.Form):
    name = forms.CharField(
        label="Ingredient name",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Enter ingredient name"
            }
        )
    )
    price = forms.DecimalField(
        required=True,
        min_value=1.00,
        decimal_places=2,
        max_digits=9,
        widget=forms.NumberInput(
            attrs={
            'placeholder':"Enter price"
            }
        )
    )
    quantity = forms.IntegerField(
        required=True,
        min_value=1,
                widget=forms.NumberInput(
            attrs={
            'placeholder':"Enter Amount"
            }
        )
    )
    measure = forms.ModelChoiceField(queryset=Measure.objects.all(),required=True,to_field_name='name')

IngredientCreationFormSet = formset_factory(IngredientForm,extra=1)
