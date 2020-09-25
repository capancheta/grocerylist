from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("meals/",views.ListMeal.as_view(),name="meal.list"),
    path("meals/new/",views.NewMeal.as_view(),name="meal.new"),
    path("meals/update/<int:meal_id>",views.UpdateMeal.as_view(),name="meal.update"),
    path("meals/delete/<int:meal_id>",views.DeleteMeal.as_view(),name="meal.delete"),
    path("recipes/",views.RecipeView.as_view(),name="recipe.list"),
    path("recipes/<int:recipe_id>/add/",views.IngredientSelectListView.as_view(),name="recipe.select.item"),
    path("recipes/<int:recipe_id>/add/<int:item_id>/",views.add_ingredient,name="recipe.add.item"),
    path("recipes/<int:recipe_id>/remove/<int:item_id>/",views.remove_ingredient,name="recipe.remove.item"),
]