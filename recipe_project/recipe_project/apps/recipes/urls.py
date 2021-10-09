from django.urls import path
from .views import CreateRecipe,CreateIngredient

urlpatterns = [
    path(
        route='create/',
        name='create',
        view=CreateRecipe.as_view()
    ),
        path(
        route='create/ingredients',
        name='ingredients',
        view=CreateIngredient.as_view()
    )
]
