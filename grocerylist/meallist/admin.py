from django.contrib import admin
from grocerylist.meallist import models

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                ]
            },
        ),
    ]
    list_display = ("id","name",)
    search_fields = ("name",)


admin.site.register(models.Recipe, RecipeAdmin)