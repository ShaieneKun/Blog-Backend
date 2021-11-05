from django.urls import path, include
from django.contrib.auth.views import LoginView
from rest_framework import routers
from .views import (
    ArticleViewSet,
    ArticlesView,
    ArticleView,
    NewArticleView,
    UpdateArticleView,
    DeleteArticleView,
)  # Use this for classes
from . import views  # Use this for functions

app_name = "blog"

router = routers.DefaultRouter()

router.register(r"api", ArticleViewSet)

urlpatterns = [
    path("", ArticlesView.as_view(), name="articles"),
    path("article/<int:pk>", ArticleView.as_view(), name="articleDetail"),
    path("article/<int:pk>/update", UpdateArticleView.as_view(), name="articleUpdate"),
    path("article/<int:pk>/delete", DeleteArticleView.as_view(), name="articleDelete"),
    path("article-form", NewArticleView.as_view(), name="articleForm"),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path("", include(router.urls)),
    # path('api-auth', include('rest_framework.urls')),
]
