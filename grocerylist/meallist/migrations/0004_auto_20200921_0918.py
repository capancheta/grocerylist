# Generated by Django 3.0.10 on 2020-09-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meallist', '0003_meals_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='type',
            field=models.CharField(choices=[('1', 'Breakfast'), ('2', 'Lunch'), ('3', 'Dinner')], max_length=30, null=True),
        ),
    ]
