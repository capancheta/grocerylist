from django.shortcuts import render
from django.http import HttpResponse
from .forms import MealNew
from grocerylist.meallist.models import Meals
from django.views.generic import ListView, CreateView

# Create your views here.

def meal_list(request):
    return HttpResponse("<b>List</b>")

class NewMeal(CreateView):
    model = Meals
    form_class = MealNew
    context_object_name = "meals"
    template_name = "meallist/new_meal.html"
    
