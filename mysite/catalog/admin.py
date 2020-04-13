from django.contrib import admin

from .models import Genre, Pig, Data
# Register your models here.

admin.site.register(Genre)

# Define the admin class
class PigAdmin(admin.ModelAdmin):
    list_display = ('pig_id', 'display_genre', 'birth', 'gender', 'dad_id', 'mom_id')
# Register the admin class with the associated model
admin.site.register(Pig, PigAdmin)

# Register the Admin classes for Data using the decorator
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'pig_id', 'weight', 'length', 'height', 'front_width', 'back_width', 'depth', 'chest', 'date')