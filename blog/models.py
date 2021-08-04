from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = MarkdownxField()

    # This defines how the instance will be called if printed
    def __str__(self):
        return self.title + " | by " + str(self.author)

    def get_absolute_url(self):
        return reverse('blog:articleDetail', kwargs={'pk': str(self.id)})
    
    
    

