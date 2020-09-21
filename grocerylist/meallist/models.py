from django.db import models

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
    date = models.DateTimeField(null=True)
    type = models.CharField(max_length=30,choices=MEAL_TYPES,null=True)
    day = models.CharField(max_length=30,choices=DAYS_OF_THE_WEEK,null=True)
    meal = models.ForeignKey(
        Recipe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="meals_recipe",
    )

    class Meta:
        db_table = "meallist_meals"

    def __str__(self):
        return self.meal


