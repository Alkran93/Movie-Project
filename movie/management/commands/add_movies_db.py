from django.core.management.base import BaseCommand
from movie.models import Movie
import json
import os

class Command(BaseCommand):
    help = 'Load movies from a JSON file'

    def handle(self, *args, **kwargs):
        json_file_path = 'movie/management/commands/movies.json'
        
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
        
        for movie in movies[:100]:  # Limitar a los primeros 100 elementos en caso de que haya menos de 100
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    genre=movie['genre'],
                    year=movie['year'],
                    short_description=movie.get('short_description', 'Default description'),  # Usamos .get() para evitar el KeyError
                    image='movie/images/default.jpg',
                )

