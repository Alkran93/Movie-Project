from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(default=2021)
    director = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.TextField(default='Default description')  # Add default here
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.jpg')
    url = models.URLField()

    def __str__(self):
        return self.title

