from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieRetrieveSerializer, MovieValidateSerializer


@api_view(['GET'])
def hello_api_view(request):
    return Response(data={'message': 'Hello, its my first Rest Api Response :)'},
                    status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()  # data from DB

        data = MovieSerializer(movies, many=True).data  # reformat data fo dict

        return Response(data=data, status=status.HTTP_200_OK)  # return data

    if request.method == 'POST':
        """1 step: validation of data """
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data=serializer.errors)
        """ 2 step: create object(operation)"""
        data = serializer.validated_data
        movie = Movie.objects.create(
            director_id=data.get('director_id'),
            title=data.get('title'),
            description=data.get('description'),
            rate=data.get('rate'),
        )
        movie.genres.set(data.get('genres'))
        """3 step: return response """
        return Response(data=MovieSerializer(movie, many=False).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def movie_retrieve_api_view(request, **kwargs):
    movie = Movie.objects.get(id=kwargs['id'])

    if request.method == 'GET':

        data = MovieRetrieveSerializer(movie, many=False).data

        return Response(data=data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = request.data

        movie.director_id = data.get('director_id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.rate = data.get('rate')

        movie.genres.set(data.get('genres'))

        movie.save()

        return Response(data=MovieRetrieveSerializer(movie, many=False).data, status=status.HTTP_200_OK)










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
