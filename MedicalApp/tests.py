from django.test import TestCase
from .models import *

class FirstTestCase(TestCase):

    def setUp(self):
        print('Setup Initiated')

    def test_one(self):
        self.assertEqual(1,1)
