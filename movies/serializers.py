from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from movies.models import Movie, Director, Genre, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'text stars'.split()


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()  # создаем новые сериализатор чтоб перевести числа в текст при выведе отзыва
    genres = GenreSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('id', 'filtered_reviews', 'director_name', 'title', 'preview', 'director', 'genres')


class MovieRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

""" 4 step validate of data """
class MovieValidateSerializer(serializers.Serializer):
    director_id = serializers.IntegerField(required=False)
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField()
    rate = serializers.FloatField(min_value=1)
    genres = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_genres(self, genres):
        genres_db = Genre.objects.filter(id__in=genres)
        if len(genres_db) != len(genres):
            raise ValidationError('Genre not found')
        return genres



    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with if {director_id} not found')
        return director_id


    # def validate(self, attrs):
    #     try:
    #         Director.objects.get(id=attrs['director_id'])
    #     except Director.DoesNotExist:
    #         raise ValidationError(f'Director with if ({attrs["director_id"]}) not found')
    #     return attrs