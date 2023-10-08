from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Source(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Video(models.Model):
    file = models.FileField(upload_to='upload', unique=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    review = models.IntegerField(null=True, blank=True)
    like = models.BooleanField(null=True, blank=True)
