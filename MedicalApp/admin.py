from django.contrib import admin
from .models import *

@admin.register(Patient)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ['id', 'lastName', 'firstName', 'age']
