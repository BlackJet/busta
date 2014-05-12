from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=1000000)
    login = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)

