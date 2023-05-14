from django.shortcuts import render
from django.contrib import messages
from movies.models import Movie
from tv_shows.models import Shows
from services import ScraperMovieService, ScraperShowsService


# Create your views here.

def index(request):
    if request.method == 'POST':
        if 'movies' in request.POST:

            service = ScraperMovieService()
            top_movies = service.get_top_movies()

            for top_movie in top_movies:
                movie = (
                    Movie.objects.filter(poster_image=top_movie.get('Poster Image:'),
                                         year=top_movie.get('Year:')).first())

                if movie:
                    movie.poster_image = top_movie.get('Poster Image:')
                    movie.rating = top_movie.get('Rating:')
                    movie.save()

                else:
                    movie = Movie(poster_image=top_movie.get('Poster Image:'),
                                  title=top_movie.get('Poster Title:'),
                                  year=top_movie.get('Year:'),
                                  rating=top_movie.get('Rating:'))

                    movie.save()
            messages.success(request, 'Successful scrapped Movies', extra_tags='success')
        elif 'shows' in request.POST:

            services = ScraperShowsService()
            top_shows = services.get_top_shows()

            for top_show in top_shows:
                show = (
                    Shows.objects.filter(poster_image=top_show.get('show_image:'),
                                         year=top_show.get('show_year:')).first())

                if show:
                    show.poster_image = top_show.get('show_image:')
                    show.rating = top_show.get('show_rating:')
                    show.save()

                else:
                    show = Shows(poster_image=top_show.get('show_image:'),
                                 title=top_show.get('show_title:'),
                                 year=top_show.get('show_year:'),
                                 rating=top_show.get('show_rating:'))
                    show.save()

            messages.success(request, 'Successful scrapped TV Shows', extra_tags='success')

    return render(request, 'core/index.html')
