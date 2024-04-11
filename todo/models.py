from django.db import models
from django.contrib.auth.models import User

class Hello(models.Model):
    id = models.AutoField(primary_key=True)
    hi = models.CharField(max_length=10)

class Todos(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField("Created At", auto_now_add=True)
    fk_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title
    
class Users(models.Model):
    username = models.CharField(max_length=30)
    password1 = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    

class AllUsers(models.Model):
    username = models.CharField(max_length=30)
    is_staff = models.BooleanField()
    email = models.EmailField()
    
class Password(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()