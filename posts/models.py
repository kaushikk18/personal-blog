from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    tag = models.CharField(max_length=10, default="null")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
