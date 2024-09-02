from django.db import models
from accounts.models import Customer

class Card(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    syllabus = models.TextField()
    