from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest import skip
from django_dynamic_fixture import G, F


class SignupViewTestCase(TestCase):

    def setUp(self) -> None:
        self.valid_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.bad_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'otherpassword',
        }

    def test_signup_successful(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(response.status_code, 302)

    def test_signup_invalid(self):
        msg = "<li>The two password fields didn"
        response = self.client.post(reverse('signup'), self.bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertTrue(msg in str(response.content))


class LoginViewTests(TestCase):
    def setUp(self):
        # Crea un usuario de prueba para usar en las pruebas
        self.user = G(
            User,
            username='testuser',
            email='testuser@mail.com',
            password='testpassword123',
        )

    @skip("Esta es tu tarea!")
    def test_login_successful(self):
        data = {
            'username': self.user.username,
            'password': self.user.password,
        }

        response = self.client.post(reverse('login'), data)
        self.user.refresh_from_db()
        print(response.content)
        self.assertEqual(response.status_code, 200)
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)

    def test_login_invalid(self):
        data = {
            'username': 'testuser',
            'password': 'incorrectpassword',
        }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
