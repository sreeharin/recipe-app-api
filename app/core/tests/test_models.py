from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_succesful(self):
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = 'sreehari@ExAmPlE.cOm'
        user = get_user_model().objects.create_user(email = email)
        self.assertEqual(user.email, 'sreehari@example.com')

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('')

    def test_create_super_user(self):
        email = 'super@example.com'
        password = 'worshipme'

        user = get_user_model().objects.create_superuser(
            email = email,
            password = password,
        )
        self.assertTrue(user.is_superuser)