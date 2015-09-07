from django.conf.urls import patterns, url
from movie_app.views import (
    get_locations,
    get_movie_locations,
    movies_list
)

urlpatterns = patterns(
    '',
    url(r'^get_movie_locations/$', get_movie_locations),
    url(r'^movie_locations/$', get_locations),
    url(r'^ac_movies/$', movies_list)
)
