from django.contrib import admin
from grocerylist.shoppinglist import models

# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
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


admin.site.register(models.Items, ItemsAdmin)