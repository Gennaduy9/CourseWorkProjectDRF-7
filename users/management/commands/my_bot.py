from django.core.management import BaseCommand

from config import settings
from useful_habits.services import send_telegram_message


# from useful_habits.services import MyBot


class Command(BaseCommand):

    def handle(self, *args, **options):
        chat_id = settings.TELEGRAM_ID  # Здесь должен быть ваш chat_id
        send_message = "Hello, it's me Gennady. My coursework is great, right?"
        return send_telegram_message(chat_id, send_message)
        # my_bot = send_telegram_message(chat_id, send_message)
        # my_bot.send_message("Hello, it's me Gennady. My coursework is great, right?")

