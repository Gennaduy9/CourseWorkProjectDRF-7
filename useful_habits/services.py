import requests

from config import settings


# class MyBot:
# """Данные для отправки telegram_message пользователю в телеграмме"""
#     URL = "https://api.telegram.org/bot"
#     TOKEN = settings.API_TELEGRAM_TOKEN
#
#     def send_message(self, text):
#         requests.post(
#             url=f'{self.URL}{self.TOKEN}/sendMessage',
#             data={
#                 'chat_id': settings.TELEGRAM_ID,
#                 'text': text
#             }
#         )


def send_telegram_message(chat_id, message):
    """Данные для отправки telegram_message пользователю в телеграмме"""

    token = settings.API_TELEGRAM_TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
