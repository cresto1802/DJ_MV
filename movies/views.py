from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie


class MovieViews(ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    #template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    '''Полное описание фильма'''
    model = Movie
    slug_field = "url"
