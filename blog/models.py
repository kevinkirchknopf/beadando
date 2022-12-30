from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

import time

    

class Post(models.Model):
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



