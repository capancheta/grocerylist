from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListMeal.as_view(),name="meal.list"),
    path("new/",views.NewMeal.as_view(),name="meal.new"),
    path("update/<int:meal_id>",views.UpdateMeal.as_view(),name="meal.update"),
    path("delete/<int:meal_id>",views.DeleteMeal.as_view(),name="meal.delete"),
]