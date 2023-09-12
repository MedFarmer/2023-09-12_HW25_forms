from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(models.Model):
    name = models.CharField(max_length=30)    
    grade = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    middle_name = models.CharField(max_length=30)    
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'