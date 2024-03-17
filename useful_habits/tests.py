from rest_framework import status
from rest_framework.test import APITestCase
from useful_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        # creating user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_create_habit(self):
        """ Habit creating testing """

        # checking that the habit is created only for authenticated users
        self.client.force_authenticate(user=self.user)

        data = {
            "action": "test habit",
            "nice_feeling": True,
            "owner": self.user
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'action': 'test habit', 'nice_feeling': True,
             'periodicity': 7, 'last_completed': None,
             'is_public': False, 'owner': None}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """ Тестируем список привычек """

        # проверка того, что привычка создана только для аутентифицированных пользователей
        self.client.force_authenticate(user=self.user)

        Habit.objects.create(
            action="test habit-list",
            nice_feeling=True,
            owner=self.user
        )
        response = self.client.get(
            '/habit/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 2, 'action': 'test habit-list',
                          'nice_feeling': True,
                          'periodicity': 7, 'last_completed': None,
                          'is_public': True, 'owner': 2}]
             }

        )

        self.assertTrue(
            Habit.objects.all().exists()
        )
