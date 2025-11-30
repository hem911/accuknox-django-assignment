from django.db import models

class CallerModel(models.Model):
    name = models.CharField(max_length=100)

class HandlerCreatedModel(models.Model):
    created_by_handler = models.BooleanField(default=True)
    note = models.CharField(max_length=200, blank=True)
