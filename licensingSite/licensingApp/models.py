from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class merchant(models.Model):
	merchantName = models.CharField(max_length=100)
	reseller = models.ForeignKey(User)

class addOns(models.Model):
	name = models.CharField(max_length=100)

class addOnDetails(models.Model):
	addOn = models.ForeignKey(addOns)
	merch = models.ForeignKey(merchant)
	isActivated = models.BooleanField(default=False)
