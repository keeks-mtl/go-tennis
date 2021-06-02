from django.db import models


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
    id = models.CharField(primary_key=True, max_length=40, null=False, blank=False)
    coach = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    spots = models.IntegerField(default=4, null=True, blank=True)
    students = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.id
