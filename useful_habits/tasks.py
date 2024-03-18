from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from .models import Habit
# from .services import MyBot
from .services import send_telegram_message


@shared_task
def check_habits_and_send_reminders():
    ''' Проверка, истек ли срок действия привычки '''
    today = timezone.now().date()
    habits = Habit.objects.all()

    for habit in habits:
        if habit.last_completed is None or \
                (today - habit.last_completed).days > habit.periodicity:
            send_email_reminder(habit.user, habit)
            send_telegram_reminder(habit.user, habit)


#             send_reminder(habit.user, habit)
#
#
# def send_reminder(user, habit):
#     my_bot = MyBot()
#     my_bot.send_message(
#         f'Пришло время применить вашу привычку: {habit.action}.'
#         f'Вы установили, что это будет происходить каждые {habit.periodicity} дней.')

# def send_reminder(user, habit):
#     send_mail(
#         subject='Время завершить свою привычку!',
#         message=f'Пришло время применить вашу привычку: {habit.action}.'
#                 f'Вы установили, что это будет происходить каждые {habit.periodicity} дней.',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[user.email],
#         fail_silently=False
#     )

def send_email_reminder(user, habit):
    """ sending email """
    send_mail(
        subject='Время завершить свою привычку!',
        message=f'Пришло время выполнить свою привычку: {habit.action}.'
                f'Вы устанавливаете, что это должно быть сделано каждый {habit.periodicity} день.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_telegram_reminder(user, habit):
    """sending telegram message"""
    if user.telegram_chat_id:
        message = f'Пришло время выполнить свою привычку: {habit.action}.' \
                  f'Вы установили, что это будет происходить каждые {habit.periodicity} дней.'
        send_telegram_message(user.telegram_chat_id, message)
