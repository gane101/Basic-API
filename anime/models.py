from django.db import models

# Create your models here.

class Anime(models.Model):
	name = models.CharField(max_length=255)
	synopsis = models.CharField(max_length=2047)
	rating = models.IntegerField()

