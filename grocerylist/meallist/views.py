from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MealNew
from grocerylist.meallist.models import Meals,Recipe
from grocerylist.meallist.filters import MealFilter
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy
from django_filters.views import FilterView
from grocerylist.shoppinglist.models import Items


# Create your views here.

class ListMeal(FilterView, ListView):
    model = Meals
    context_object_name = "meals"
    template_name = "meallist/list_meal.html"
    filterset_class = MealFilter

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

    
class UpdateMeal(UpdateView):
    model = Meals
    form_class = MealNew
    context_object_name = "meals"
    template_name = "meallist/new_meal.html"
    pk_url_kwarg = "meal_id"

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.updated_at = timezone.now()
        meal.save()
        return redirect('meal.list',)    


class DeleteMeal(DeleteView):
    model = Meals
    pk_url_kwarg = "meal_id"
    context_object_name = "meal"
    success_url = reverse_lazy('meal.list')
    template_name  = "meallist/delete_meal.html"


class RecipeView(ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "meallist/list_recipes.html"

    def get_queryset(self):
        return super().get_queryset().order_by("name")    


class IngredientSelectListView(ListView):
    model = Items
    context_object_name = "items"
    template_name = "meallist/list_items_select.html"

    def get_context_data(self, **kwargs):
        kwargs['recipe_id'] = self.kwargs.get('recipe_id')
        return super().get_context_data(**kwargs)


def add_ingredient(request, recipe_id, item_id):
    recipe = Recipe.objects.get(id=recipe_id)
    item = Items.objects.get(id=item_id)

    recipe.ingredients.add(item)
    recipe.save()

    return redirect("recipe.list")

def remove_ingredient(request, recipe_id, item_id):
    recipe = Recipe.objects.get(id=recipe_id)
    item = Items.objects.get(id=item_id)

    recipe.ingredients.remove(item)
    recipe.save()

    return redirect("recipe.list")


def home(request):
    return render(request,"meallist/home.html",{"message" : "Home Menu Planner"})