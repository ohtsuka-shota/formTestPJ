from django.db import models

class MyCreateTable(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    memo = models.CharField(max_length=255)