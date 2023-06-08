from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieRetrieveSerializer


@api_view(['GET'])
def hello_api_view(request):
    return Response(data={'message': 'Hello, its my first Rest Api Response :)'},
                    status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()  # data from DB

    data = MovieSerializer(movies, many=True).data  # reformat data fo dict

    return Response(data=data, status=status.HTTP_200_OK)  # return data


@api_view(['GET'])
def movie_retrieve_api_view(request, **kwargs):
    movie = Movie.objects.get(id=kwargs['id'])

    data = MovieRetrieveSerializer(movie, many=False).data

    return Response(data=data, status=status.HTTP_200_OK)

"""

LIST_OF_MOVIES = [
    {
        "id": 1
        "title": "title 1",
        "description": "awdawd",
        "preview" "/media/previews/movie1.jpg"
    },
    {
        "id": 1
        "title": "title 1",
        "description": "awdawd",
        "preview" "/media/previews/movie1.jpg"
    }
]

MOVIE_1 = {
    "id": 1
    "title": "title 1",
    "description": "awdawd",
    "preview" "/media/previews/movie1.jpg"
}

"""


