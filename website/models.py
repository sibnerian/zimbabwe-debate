from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    image_url = models.URLField()

class Sponsor(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    image_url = models.URLField()