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
    description = forms.CharField(
        label="Recipe description",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Enter recipe description"
            }
        )
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(),required=True,to_field_name='name')
    image = forms.ImageField()
    extra_category_count = forms.CharField(widget=forms.HiddenInput())
    ingredients = forms.ModelChoiceField(queryset=IngPrice.objects.all(),required=True)

    def __init__(self,*args, **kwargs):
        extra_category = kwargs.pop('extra',0)
        ing = forms.ModelChoiceField(queryset=IngPrice.objects.all(),required=True)
        if not extra_category:
            extra_category=0
        super(RecipeForm,self).__init__(*args, **kwargs)
        self.fields['extra_category_count'].initial = extra_category

        for i in range(int(extra_category)):
            self.fields[f'extra_category_{i}']=ing



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
