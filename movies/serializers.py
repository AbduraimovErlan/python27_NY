from rest_framework import serializers

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