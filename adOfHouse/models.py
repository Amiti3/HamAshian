from django.db import models
from django.contrib.auth.models import User
from house.models import House
from datetime import datetime


class AdOfHouse(models.Model):
    price = models.IntegerField()
    user1 = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    house1 = models.ForeignKey(House, null=False, on_delete=models.CASCADE)
    personalInfo = models.TextField()
    date_publish = models.DateField(default=datetime.today())
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.user1.username + self.house1.region
