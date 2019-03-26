import datetime

from django.db import models


class New(models.Model):
    headline = models.CharField(max_length=50)
    content = models.TextField()
    photo = models.URLField()
    data = models.DateField()






