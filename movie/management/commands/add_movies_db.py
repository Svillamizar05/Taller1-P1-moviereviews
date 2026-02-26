from django.core.management.base import BaseCommand
from movie.models import Movie
import json


class Command(BaseCommand):
    help = 'Load movies from movies.json into the Movie model'

    def handle(self, *args, **kwargs):
        json_file_path = 'movie/management/commands/movies.json'

        with open(json_file_path, 'r', encoding='utf-8') as file:
            movies = json.load(file)

        for i in range(100):
            movie = movies[i]

            exists = Movie.objects.filter(title=movie['title']).first()

            if not exists:
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/default.jpg',
                    genre=movie['genre'],
                    year=movie['year'],
                    description=movie['plot']
                )

        self.stdout.write(self.style.SUCCESS('Movies loaded successfully.'))