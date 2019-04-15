from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from budgets.models import Budget, Transaction
from django.contrib.auth.models import User
from budgets_api.views import RegisterApiView, UserAPIView, BudgetListAPIView, TransactionListAPIView
import json


class TestUserAPI(TestCase):
    def test_user_registration(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        response = self.client.post('/api/v1/register', user)
        self.assertIn(b'"username":"test_user"', response.content)

    def test_user_login(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        token = json.loads(response.content)

        self.assertEqual(len(token['token']), 40)

    def test_user_registration_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        response = self.client.post('/api/v1/register', user)
        self.assertEqual(response.status_code, 201)

    def test_user_login_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.assertEqual(response.status_code, 200)


class TestBudgetApi(APITestCase):

    def test_get_budgets(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        user = User.objects.get(username='test_user')
        view = BudgetListAPIView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/api/v1/budget/')
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Budget.objects.all()), 0)

class TestTransactionApi(APITestCase):
    def test_get_transaction(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        user = User.objects.get(username='test_user')
        view = TransactionListAPIView.as_view()
        factory = APIRequestFactory()
        request = factory.get('/api/v1/transaction/')
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Budget.objects.all()), 0)


