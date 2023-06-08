from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='director_movies')
    genres = models.ManyToManyField(Genre, blank=True)
    preview = models.ImageField(upload_to='previews')
    title = models.CharField(max_length=256)
    description = models.TextField()
    rate = models.FloatField(default=0)

    @property
    def filtered_reviews(self):
        # return self.reviews.filter(stars__gte=3)
        return Review.objects.filter(movie=self, stars__gt=3)

    @property
    def director_name(self):  # делаем функции в моделки чтоб выташить только название без ничего
        # try:
        #     return self.director.name
        # except:
        #     return None
        return self.director.name if self.director else ""


STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES, null=True)

    def __str__(self):
        return self.text