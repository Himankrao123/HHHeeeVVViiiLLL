from django.db import models

# Create your models here.
class Trap(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
class Newtrap(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    number = models.IntegerField()
    def __str__(self):
        return self.username