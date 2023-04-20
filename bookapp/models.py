import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class bookmodel(models.Model):
    bookname=models.CharField(max_length=30)
    bookpdf =models.FileField(upload_to='bookapp/static')
    bookimage=models.FileField(upload_to='bookapp/static')
    author=models.CharField(max_length=30)
    bookdate=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.bookname
