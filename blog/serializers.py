from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ("username", "email")

class PostSerializer(serializers.HyperlinkedModelSerializer):
	author = UserSerializer()

	class Meta:
		model = Post
		fields = ("id", "title", "author", "body")
