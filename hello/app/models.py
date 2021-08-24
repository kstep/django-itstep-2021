from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(
        max_length=200)
    group = models.IntegerField()
    birthday = models.DateField()
    last_name = models.CharField(max_length=200)


