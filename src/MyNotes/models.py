from django.db import models

# Create your models here.
class SamedNotes(models.Model):
    day = models.CharField(max_length=20)
    notes = models.TextField()
    date = models.DateField(blank=True, null=True)
class MamadouNotes(models.Model):
    day = models.CharField(max_length=20)
    notes = models.TextField()
    date = models.DateField(blank=True, null=True)