from django.db import models

class SignBase (models.Model):
    public_key = models.FileField()
    private_key = models.FileField()
    subject_name = models.CharField(max_length=100)