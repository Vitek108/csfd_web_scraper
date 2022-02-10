from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Actors(models.Model):
    name = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movies, related_name="actors")

    def __str__(self):
        return self.name

