from django.db import models


class SongInChart(models.Model):
    author = models.CharField(max_length=30)
    song = models.CharField(max_length=30)
    position = models.PositiveIntegerField(unique=True)