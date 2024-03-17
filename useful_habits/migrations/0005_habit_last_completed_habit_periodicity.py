# Generated by Django 5.0.3 on 2024-03-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("useful_habits", "0004_remove_feeling_nice_feeling_habit_nice_feeling"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="last_completed",
            field=models.DateField(
                blank=True, null=True, verbose_name="Последний срок"
            ),
        ),
        migrations.AddField(
            model_name="habit",
            name="periodicity",
            field=models.IntegerField(
                default=7, verbose_name="Частота выполнения привычки"
            ),
        ),
    ]