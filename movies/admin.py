from django.contrib import admin
from .models import Category, Movie, MovieShots, Genre, RatingStar, Rating, Reviews, Actor

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Genre)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
admin.site.register(Actor)
