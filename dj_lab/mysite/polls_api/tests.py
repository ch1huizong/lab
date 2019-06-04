from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from polls_api import views


"""
class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls-api/polls/'
        self.user = self.setup_user()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='test@gmail.com',
            password='1234test',
        )

    def test_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertSetEqual(
            response.status_code, 
            200,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
"""
class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/polls-api/polls/'

    def test_list2(self):
        self.client.login(username='dj', password='1234test')
        response = self.client.get(self.uri)
        self.assertSetEqual(
            response.status_code, 
            200,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )

    def test_create(self):
        self.client.login(username='dj', password='1234test')
        params = {
            'question': 'How are you?',
            'created_by': 1,
        }
        response = self.client.post(self.uri, params)
        self.assertSetEqual(
            response.status_code, 
            200,
            'Expected Response Code 200, received {0} instead.'.format(response.status_code)
        )
