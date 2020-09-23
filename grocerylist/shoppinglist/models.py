from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=50,null=False)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "meallist_items"
    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    date = models.DateField(null=False)
    item = models.ForeignKey(
        Items,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="meals_shoppinglist",
    )
    notes = models.CharField(max_length=50,null=False)

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Lists"
        db_table = "meallist_lists"
    def __str__(self):
        return f"{self.date} - {self.item.name}"
