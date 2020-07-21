from django.test import TestCase
from django.contrib.auth.models import User
import unittest

class MyTesting(unittest.TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.up1 = UserProfile.objects.create(user=self.u1)

    def testA(self):
        self.u1.get_full_name()

    def tearDown(self):
        self.up1.delete()
        self.u1.delete()