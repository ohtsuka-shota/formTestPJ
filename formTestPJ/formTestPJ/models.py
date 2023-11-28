from django.db import models

class MyFormTable(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    memo = models.CharFied(max_length=255)