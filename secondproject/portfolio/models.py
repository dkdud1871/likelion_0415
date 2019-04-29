from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name=models.CharField(max_length=50, verbose_name='이름')
    age=models.IntegerField(verbose_name='나이')
    major=models.CharField(max_length=50, verbose_name='전공')
    grade=models.CharField(max_length=50, verbose_name='학년')
    hometown=models.CharField(max_length=50, verbose_name='고향')
    def __str__(self):
        return self.name
    