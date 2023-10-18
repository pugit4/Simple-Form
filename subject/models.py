from django.db import models

# Create your models here.
class Mytopic(models.Model):
    topic = models.CharField(max_length=255)
    description = models.TextField()