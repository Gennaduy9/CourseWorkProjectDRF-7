# Generated by Django 5.0.3 on 2024-03-15 13:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
        migrations.CreateModel(
            name="Feeling",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(max_length=255, verbose_name="Место действия"),
                ),
                (
                    "action_datetime",
                    models.DateTimeField(verbose_name="Данные и время действия"),
                ),
                ("action", models.CharField(max_length=255, verbose_name="Действие")),
                (
                    "nice_feeling",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятного чувства"
                    ),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[("week", "once a week"), ("every_day", "every day")],
                        default="every_day",
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(verbose_name="Время завершения"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="useful_habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Чувство",
                "verbose_name_plural": "Чувства",
            },
        ),
    ]
