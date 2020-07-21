from django.db import models

class House(models.Model):
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    address = models.TextField()
    houseArea = models.IntegerField()
    roommmateNum = models.IntegerField()
    roomNum = models.IntegerField()
    wcNum = models.IntegerField()
    ageOfHouse = models.IntegerField()

    def __str__(self):
        return self.city + self.region
