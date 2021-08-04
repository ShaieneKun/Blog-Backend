from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ("username", "email")

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	author = UserSerializer()

	class Meta:
		model = Article
		fields = ("id", "title", "author", "body")
