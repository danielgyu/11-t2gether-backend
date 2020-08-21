import json
import unittest

from django.test import Client, TestCase

client = Client()

class UnitTest(TestCase):
    test_user_data = {
        'first_name'               : 'TEST1',
        'last_name'                : 'Mr1',
        'phone'                    : '010-1111-0101',
        'email'                    : 'MrTEST1@email.com',
        'password'                 : '1q2w3e4r5t6ASD',
        'birthdate'                : '2020-08-20',
        'is_newsletter_subscribed' : False
        }
    def test_JoinView(self):
        response = client.post('/user/join', json.dumps(self.test_user_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_LoginView(self):
        client.post('/user/join', json.dumps(self.test_user_data), content_type = 'application/json')
        test_login_data = {
            'email'    : 'MrTEST1@email.com',
            'password' : '1q2w3e4r5t6ASD'
        }

        response = client.post('/user/login', json.dumps(test_login_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
