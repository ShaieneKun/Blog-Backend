from django.contrib import admin
from django.urls import path, include

# from markdownx import urls as markdownx_urls
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
import debug_toolbar
from blog import views

# REST framework's paths
rest_router = routers.DefaultRouter()
rest_router.register("articles", views.ArticleSerializedView, "articles")

urlpatterns = [
    path("", include("index.urls", namespace="index")),
    path("admin/", admin.site.urls),
    path("api/", include(rest_router.urls)),
    path("blog/", include("blog.urls", namespace="blog")),
    path("users/", include("users.urls", namespace="users")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api-token-auth/', obtain_auth_token),
]
