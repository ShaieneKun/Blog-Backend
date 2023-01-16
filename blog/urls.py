from django.urls import path, include
from django.contrib.auth.views import LoginView
from rest_framework import routers
from .views import (
    ArticleSerializedView,
    AuthArticleSerializedView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)  # Use this for classes
from . import views  # Use this for functions

app_name = "blog"

api_auth_router = routers.DefaultRouter()
api_router = routers.DefaultRouter()

api_auth_router.register(r"api", AuthArticleSerializedView)
api_router.register(r"api", ArticleSerializedView)

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="articleDetail"),
    path("article/<int:pk>/update", ArticleUpdateView.as_view(), name="articleUpdate"),
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="articleDelete"),
    path("article-form", ArticleCreateView.as_view(), name="articleForm"),
    path(
        "accounts/login/",
        LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path("", include(api_router.urls)),
    path("auth/", include(api_auth_router.urls)),
    # path('api-auth', include('rest_framework.urls')),
]
