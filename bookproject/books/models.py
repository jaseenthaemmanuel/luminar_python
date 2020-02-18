from django.db import models

# Create your models here.
class Bookmodel(models.Model):

    bookname = models.CharField(max_length=200)
    page = models.IntegerField()

    def __str__(self):

        return self.bookname
