from django import forms
from grocerylist.meallist.models import Meals

class MealNew(forms.ModelForm):
    class Meta:
        model = Meals
        fields = [
            "date",
            "type",
            "day",
            "meal"
        ]