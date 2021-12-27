from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MarkdownxField()
    tags = models.ManyToManyField("Tag")

    def __str__(self) -> str:
        return f"{self.title} • by {self.author}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default=None)
    colour = models.CharField(max_length=7, default="#888888")

    def __str__(self) -> str:
        return f"{self.name} • {self.colour}"
