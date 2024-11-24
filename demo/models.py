from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.TextField()
    username = models.TextField()
    balance = models.FloatField()
    # TODO: Create relationship to Transaction model

    def __str__(self):
        return self.name
    
# TODO: Create Transaction Model