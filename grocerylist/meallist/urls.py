from django.urls import path
from . import views

urlpatterns = [
    path("",views.meal_list,name="meal.list"),
    path("new/",views.NewMeal.as_view(),name="meal.new"),
]