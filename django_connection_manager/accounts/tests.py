from django.test import TestCase
from django.urls import reverse
import json

class SignupTests(TestCase):
    def test_signup_success(self):
        # Adjust the URL if needed.
        url = '/accounts/signup/'
        data = {"username": "testuser", "password": "testpass"}
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        json_response = response.json()
        self.assertIn("access", json_response)
        self.assertIn("refresh", json_response)

class LogoutTests(TestCase):
    def setUp(self):
        self.signup_url = '/accounts/signup/'
        data = {"username": "testuser", "password": "testpass"}
        res = self.client.post(self.signup_url, json.dumps(data), content_type="application/json")
        tokens = res.json()
        self.access_token = tokens['access']
        self.refresh_token = tokens['refresh']

    def test_logout_success(self):
        url = '/accounts/logout/'
        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.access_token
        data = {"refresh": self.refresh_token}
        response = self.client.post(url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get("message"), "Logout successful")

class LoginTests(TestCase):
    def setUp(self):
        self.signup_url = '/accounts/signup/'
        # Create user for login test
        data = {"username": "loginuser", "password": "loginpass"}
        self.client.post(self.signup_url, json.dumps(data), content_type="application/json")
        self.login_url = '/accounts/login/'

    def test_login_success(self):
        data = {"username": "loginuser", "password": "loginpass"}
        response = self.client.post(self.login_url, json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn("access", json_response)
        self.assertIn("refresh", json_response)
