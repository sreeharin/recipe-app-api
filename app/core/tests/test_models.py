from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def create_user(email='user@example.com', password='testpass123'):
    return get_user_model().objects.create_user(email, password)


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

    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user = user,
            title = 'Sample recipe',
            time_minutes = 5,
            price = Decimal('5.50'),
            description = 'Sample recipe description',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag 1')
        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient 1',
        )
        self.assertEqual(str(ingredient), ingredient.name)