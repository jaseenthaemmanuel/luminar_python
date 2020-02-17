from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    desig = models.CharField(max_length=100)
    phonenum = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    verify_password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


