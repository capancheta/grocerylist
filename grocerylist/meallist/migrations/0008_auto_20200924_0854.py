# Generated by Django 3.0.10 on 2020-09-24 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0001_initial'),
        ('meallist', '0007_auto_20200923_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='recipe_items', to='shoppinglist.Items'),
        ),
        migrations.AlterField(
            model_name='meals',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 8, 54, 14, 98480, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='meals',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 8, 54, 14, 98513, tzinfo=utc)),
        ),
    ]