import os
from django.db import models
from django.contrib.auth.models import User



def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.name + os.path.splitext(filename)[1])

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=6)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=avatar_upload_to)
# Create your models here.

class Book_user(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

