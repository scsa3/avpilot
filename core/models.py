from django.db import models


class Video(models.Model):
    path = models.FilePathField()
    porn_id = models.CharField(max_length=100)
    # height = models.IntegerField()
    # width = models.IntegerField()
    # format = models.CharField(max_length=10)

