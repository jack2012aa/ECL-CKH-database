from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class Pig(models.Model):
    pig_id = models.CharField(max_length=8,primary_key=True, help_text='Input birth year(XX) + ear tag')
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100)
    dad_id = models.CharField(max_length=100)
    mom_id = models.CharField(max_length=100)
    breed = models.CharField(max_length=10, help_text='Pig\'s breed', blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('pig-detail', args=[str(self.pig_id)])

    def __str__(self):
        """String for representing the Model object."""
        # return f'{self.pig_id}'
        return self.pig_id
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

class Pig_history(models.Model):
    pig_id = models.CharField(null = True, max_length=8, help_text='Input birth year(XX) + ear tag')
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, max_length=100)
    dad_id = models.CharField(null=True, max_length=100)
    mom_id = models.CharField(null=True, max_length=100)
    breed = models.CharField(max_length=10, help_text='Pig\'s breed', blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String for representing the Model object."""
        # return f'{self.pig_id}'
        return self.pig_id

class Data(models.Model):
    """Model representing measuring datas."""
    data_id = models.AutoField(primary_key=True)
    pig_id = models.ForeignKey('Pig', on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(help_text='Input weight in kg.')
    length = models.FloatField(help_text='Input body length in cm.')
    height = models.FloatField(help_text='Input height in cm.')
    front_width = models.FloatField(help_text='Input front width in cm.')
    back_width = models.FloatField(help_text='Input back width in cm.')
    depth = models.FloatField(help_text='Input body depth in cm.') 
    chest = models.FloatField(help_text='Input chest in cm.')   
    front_cannon_circumference = models.FloatField(
        help_text='Input front cannon circumference in cm.',
        null=True,
        )
    back_cannon_circumference = models.FloatField(
        help_text='Input front cannon circumference in cm.',
        null=True,
        )
    date = models.DateField(
        help_text='Input measuring date.',
        null=True,
        )   

    def __str__(self):
        """String for representing the Model object."""
        return str(self.data_id)
    
class Data_history(models.Model):
    """Model representing measuring datas."""
    data_id = models.IntegerField(null=True)
    pig_id = models.ForeignKey('Pig', on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(null=True)
    length = models.FloatField(null=True)
    height = models.FloatField(null=True)
    front_width = models.FloatField(null=True)
    back_width = models.FloatField(null=True)
    depth = models.FloatField(null=True) 
    chest = models.FloatField(null=True)   
    front_cannon_circumference = models.FloatField(null=True)
    back_cannon_circumference = models.FloatField(null=True)
    date = models.DateField(null=True)   
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.data_id)