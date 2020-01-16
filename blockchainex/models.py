# Create your models here.
from django.db import models


class Block(models.Model):
    hash = models.CharField(max_length=64)
    confirmations = models.IntegerField()
    timestamp = models.DateTimeField()
    height = models.BigIntegerField()
    numOfTrx = models.IntegerField()
    difficulty = models.DecimalField(decimal_places=2, max_digits=12)
    merkleRoot = models.CharField(max_length=64)
    version = models.CharField(max_length=64)
    bits = models.BigIntegerField()
    weight = models.BigIntegerField()
    size = models.BigIntegerField()
    nonce = models.BigIntegerField()


class Tx(models.Model):
    hash = models.CharField(max_length=64)
    timestamp = models.DateTimeField()
    size = models.BigIntegerField()
    weight = models.BigIntegerField()
    blockHash = models.CharField(max_length=64)
    confirmations = models.IntegerField()


class Payload(object):
    def __init__(self, action, method, data):
        self.action = action
        self.method = method
        self.data = data
