from django.db import models

class Movie(models.Model):
    preview = models.ImageField(upload_to='previews')
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)

