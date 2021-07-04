from django.db import models
from django.contrib.auth.models import User

from coaches.models import Coach
from profiles.models import UserProfile


class ClassType(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Lesson(models.Model):
    class_type = models.ForeignKey(
        'ClassType', null=True, blank=True, on_delete=models.SET_NULL)
    coach = models.ForeignKey(Coach, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    date = models.DateField(default="2021-09-05")
    time = models.TimeField()
    spots = models.IntegerField(default=4)
    students = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id
