from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import home

class motorhomeTests(TestCase):

    @classmethod

    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='admin', password='admin1234')
        testuser1.save()

        test_home = home.objects.create(
            owner = testuser1,
            title = 'home1',
            specification = 'home1home1home1home1home1.'
        )
        test_home.save()

    def test_home_content(self):
        rv = home.objects.get(id=1)
        actual_owner = str(rv.owner)
        actual_title = str(rv.title)
        actual_specification = str(rv.specification)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_title, 'home1')
        self.assertEqual(actual_specification, 'home1home1home1home1home1')
        