from django.db import models
import fsb795

class SignBase (models.Model):
    public_key = models.FileField()
    private_key = models.FileField()
    final = fsb795.Certificate(public_key)
    subject_name = models.CharField(max_length=100)
    date_final = models.DateTimeField(final.validityCert())
    
