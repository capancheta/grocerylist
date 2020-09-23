from django.db import models
from django.utils import timezone

# Create your models here.

MEAL_TYPES = (
    ('1','Breakfast'),
    ('2','Lunch'),
    ('3','Dinner')
)

DAYS_OF_THE_WEEK = (
    ("Monday","Monday"),
    ("Tuesday","Tuesday"),
    ("Wednesday","Wednesday"),
    ("Thursday","Thursday"),
    ("Friday","Friday"),
    ("Saturday","Saturday"),
    ("Sunday","Sunday"),
)


class Recipe(models.Model):
    name = models.CharField(max_length=50,null=False)
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        db_table = "meallist_recipes"
    def __str__(self):
        return self.name


class Meals(models.Model):
    date = models.DateField(null=False)
    type = models.CharField(max_length=30,choices=MEAL_TYPES,null=True)
    day = models.CharField(max_length=30,choices=DAYS_OF_THE_WEEK,null=True)
    meal = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="meals_recipe",
    )
    created_at = models.DateTimeField(default=timezone.now(),null=False)
    updated_at = models.DateTimeField(default=timezone.now(),null=False)

    class Meta:
        db_table = "meallist_meals"

    def __str__(self):
        return f"{self.date} - {self.day} - {self.meal.name}"


