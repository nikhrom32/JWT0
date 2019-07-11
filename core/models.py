from django.db import models

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(max_length=40, default='', blank=True)
    password = models.CharField(max_length=20)
