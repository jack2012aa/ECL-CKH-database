from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(blank=True)
#     file = models.ImageField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Pig(models.Model):
    """Model representing an author."""
    pig_id = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this pig')
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100)
    dad_id = models.CharField(max_length=100)
    mom_id = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.pig_id}'
    
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Data(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    pig_id = models.ForeignKey('Pig', on_delete=models.SET_NULL, null=True)
    
    # Foreign Key used because a data can only belong to one pig, but a pig can have multiple datas
    # Pig as a string rather than object because it hasn't been declared yet in the file.
    weight = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    front_width = models.CharField(max_length=100)
    back_width = models.CharField(max_length=100)
    depth = models.CharField(max_length=100)
    chest = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    
    # ManyToManyField used because genre can contain many books. pigs can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
