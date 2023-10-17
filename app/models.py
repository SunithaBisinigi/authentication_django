from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
 # Make sure this line is present
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Consider using a more secure way to store passwords

# # Create your models here.
# class Member(models.Model):
#     firstname=models.CharField(max_length=225)
#     lastname=models.CharField(max_length=225)
#     phone = models.IntegerField(null=True)
#     joined_date = models.DateField(null=True)