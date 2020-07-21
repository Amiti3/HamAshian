from django.test import TestCase
import unittest
from adOfRoommate.models import *

class Test1(unittest.TestCase):

    def setUp(self):
        self.a1 = AdOfRoommate.objects.create(priceMin=100, priceMax=300)

    def testA(self):
        self.a1.get_full_name()

    def tearDown(self):
        self.a1.delete()
