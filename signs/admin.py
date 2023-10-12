from django.contrib import admin
from .models import SignBase

# Register your models here.

@admin.register (SignBase)
class AdminSignBase(admin.ModelAdmin):
    list_display = ('subject_name', 'public_key')
