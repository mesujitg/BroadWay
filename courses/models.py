from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    details = models.TextField()
    fee = models.FloatField()

