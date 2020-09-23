import django_filters
from grocerylist.meallist.models import Meals


class MealFilter(django_filters.FilterSet):

    class Meta:
        model = Meals
        fields = {            
            'meal__name': ['icontains'],
            'day' : ['icontains'],
        }

