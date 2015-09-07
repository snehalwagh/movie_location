from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
from movie_app.models import Movie

def get_movie_locations(request):
    if request.method == 'GET':
        movie_name = request.GET.get('movie_id')
        locations = Movie.objects.filter(
            title=movie_name
            ).values_list('location')

        address = locations[0][0]
        if not address:
            return HttpResponse(
                'no_results',
                content_type="application/json"
            )
        data = [['Address']] + [
            [loc[0] + ', San Francisco, California'] for loc in locations
        ]
        return HttpResponse(
            json.dumps(data),
            content_type="application/json"
        )

def get_locations(request):
    return render_to_response("map_longlat.html")


def movies_list(request):
    query = request.REQUEST.get('term', None)
    if query:
        movies = Movie.objects.filter(
            title__icontains=query
        ).values_list('title', flat=True)[:15]
    return HttpResponse(
        json.dumps(list(set(movies))),
        content_type="application/json"
    )

