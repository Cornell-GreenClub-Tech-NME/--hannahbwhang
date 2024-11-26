from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.TextField()
    username = models.TextField()
    balance = models.FloatField()

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    #id = models.TextField()
    amount = models.FloatField()
    senderid = models.ForeignKey(User, related_name="sent_transactions", on_delete=models.CASCADE)
    receiverid = models.ForeignKey(User, related_name="received_transactions", on_delete=models.CASCADE )
    pending = models.BooleanField()