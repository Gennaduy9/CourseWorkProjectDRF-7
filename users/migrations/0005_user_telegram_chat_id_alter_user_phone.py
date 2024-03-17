# Generated by Django 5.0.3 on 2024-03-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_first_name_alter_user_last_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="telegram_chat_id",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Telegram chat ID"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                unique=True,
                verbose_name="Телефон",
            ),
        ),
    ]