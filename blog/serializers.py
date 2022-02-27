from os import read
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class ArticleSerializer(serializers.ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Article
        fields = "__all__"  # ("id", "title", "author", "body")
