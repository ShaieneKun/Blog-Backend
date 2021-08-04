from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from .models import Article
from .forms import ArticleForm
from .serializers import ArticleSerializer

# REST Views

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

# Class views

# See docs for ListView
# Lists all Articles
class ArticlesView(ListView):
    model = Article
    template_name = "Articles/home.html"

# See docs for DetailView
# Show the article in full detail
class ArticleView(DetailView):
    model = Article
    template_name = "Articles/articleDetail.html"

# See docs for LoginRequiredMixin, UpdateView and reverse_lazy
# Allows user to change the content of the article
class UpdateArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'Articles/ArticleForm.html'
    # form_class = ArticleForm
    login_url = reverse_lazy('blog:login')
    fields = ['title','body']
    success_url = reverse_lazy('blog:Articles')

# See docs for LoginRequiredMixin and CreateView
# Allows user to create a new Article
class NewArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'Articles/ArticleForm.html'
    form_class = ArticleForm
    login_url = reverse_lazy('blog:login')

    # Overriding form_valid to associate the user to the Article
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    login_url = reverse_lazy('blog:login')
    success_url = reverse_lazy('blog:Articles')