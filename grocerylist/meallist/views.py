from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MealNew
from grocerylist.meallist.models import Meals
from django.views.generic import ListView, CreateView
from django.utils import timezone

# Create your views here.

# def meal_list(request):    
#     return HttpResponse("<b>List</b>")

class ListMeal(ListView):
    model = Meals
    context_object_name = "meals"
    template_name = "meallist/list_meal.html"

    def get_queryset(self):
        return super().get_queryset().order_by("date","type")


class NewMeal(CreateView):
    model = Meals
    form_class = MealNew
    context_object_name = "meals"
    template_name = "meallist/new_meal.html"

    def get_initial(self):
        initial_data = super(NewMeal, self).get_initial()
        initial_data['date'] = timezone.now()
        initial_data['day'] = initial_data['date'].strftime("%A")

        return initial_data

    def form_valid(self, form):
        data = form.save(commit=False)
        meal = Meals.objects.create(
            date=data.date,
            type=data.type,
            day=data.day,
            meal=data.meal
        )
        meal.save()
        return redirect("meal.list")

    
