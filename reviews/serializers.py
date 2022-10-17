from rest_framework import serializers

from .models import Review


class CriticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ["id", "movie", "critic"]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
