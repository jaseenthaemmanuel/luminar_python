from django.db import models

class LoginModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sal = models.IntegerField()
    desig = models.CharField(max_length=100)
    phone = models.IntegerField()
    usrnm = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.name