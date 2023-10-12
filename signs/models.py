from django.db import models

class SignBase (models.Model):
    public_key = models.FileField()