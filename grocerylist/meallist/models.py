from django.db import models

# Create your models here.

MEAL_TYPES = (
    ('Breakfast','Breakfast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner')
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

class Meals(models.Model):
    type = models.CharField(max_length=30,choices=MEAL_TYPES,null=True)
    day = models.CharField(max_length=30,choices=DAYS_OF_THE_WEEK,null=True)
    meal = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "meallist_meals"

    def __str__(self):
        return self.meal
