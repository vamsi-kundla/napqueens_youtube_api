from django.db import models

# Create your models here.

class Youtube_search(models.Model):
    video_title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    published_datetime = models.CharField(max_length=300)
    thumbnail_url = models.CharField(max_length=300)
    query = models.CharField(max_length=300)
