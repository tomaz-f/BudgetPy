from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique = True, blank = True)
    budget = models.IntegerField()