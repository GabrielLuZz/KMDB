from pydoc import synopsis
from rest_framework import serializers
from genres.models import Genre

from genres.serializers import GenreSerializer
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genres = validated_data.pop("genres")

        genres = [
            Genre.objects.get_or_create(name=genre["name"])[0] for genre in genres
        ]

        movie = Movie.objects.create(**validated_data)

        movie.genres.set(genres)

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        genres = validated_data.pop("genres")

        genres = [
            Genre.objects.get_or_create(name=genre["name"])[0] for genre in genres
        ]

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        instance.genres.set(genres)

        return instance
