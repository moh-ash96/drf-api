from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import DateField

class Movie(models.Model):
    name = models.CharField(max_length=64)
    rate = models.FloatField()
    release = models.DateField()
    genre = models.CharField(max_length=64)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
