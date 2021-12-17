from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes: models.PositiveBigIntegerField(default=0)

class User(models.Model):
    pass