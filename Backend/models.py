from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    user_id = models.CharField(max_length=7)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
