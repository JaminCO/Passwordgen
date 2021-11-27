from django.db import models

# Create your models here.
class Passcode(models.Model):
    password = models.CharField(max_length=80, blank=True)
    created = models.DateTimeField(auto_now=True)