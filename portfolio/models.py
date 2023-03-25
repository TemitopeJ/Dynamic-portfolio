from django.db import models

# Create your models here.
class Project(models.Model):
    img_url = models.CharField(max_length=4000)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    link = models.URLField(max_length=1000)


class Skill(models.Model):
    img_url = models.CharField(max_length=4000)
    text = models.CharField(max_length=50)

class About(models.Model):
    text = models.CharField(max_length=1000)