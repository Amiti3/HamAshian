from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class AdOfRoommate(models.Model):
    priceMin = models.IntegerField()
    priceMax = models.IntegerField()
    user1 = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    personalInfo = models.TextField()
    date_publish = models.DateField(default=datetime.today())
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user1.username)