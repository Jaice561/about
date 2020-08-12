from django.db import models

# Create your models here.
class Photo(model.Model):
    image = models.BinaryField(blank=True)
