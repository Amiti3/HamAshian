from django.test import TestCase
from house.models import House

class MyTesting(unittest.TestCase):

    def setUp(self):
        self.u1 = House.objects.create(ageOfHouse=13, houseArea=2)

    def testA(self):
        self.u1.get_full_name()

    def tearDown(self):
        self.up1.delete()
        self.u1.delete()
