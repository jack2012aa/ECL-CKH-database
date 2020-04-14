from django.contrib import admin

from .models import Pig, Data
# Register your models here.

# Define the admin class

@admin.register(Pig)
class PigAdmin(admin.ModelAdmin):
    list_display = ('pig_id', 'breed', 'birth', 'gender', 'dad_id', 'mom_id')
# Register the admin class with the associated model

# Register the Admin classes for Data using the decorator
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('data_id', 'pig_id', 'weight', 'length', 'height', 'front_width', 'back_width', 'depth', 'chest', 'front_cannon_circumference', 'back_cannon_circumference','date')
