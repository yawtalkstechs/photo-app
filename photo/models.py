from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/profile_pics')