"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from django_markdownx import urls as markdownx_urls
from rest_framework import routers
from blog import views

import debug_toolbar
from main import settings

# REST framework's paths
rest_router = routers.DefaultRouter()
rest_router.register("articles", views.ArticleSerializedView, "articles")

urlpatterns = [
    path("index/", include("index.urls", namespace="index")),
    path("admin/", admin.site.urls),
    path("api/", include(rest_router.urls)),
    path("blog/", include("blog.urls", namespace="blog")),
    # path("markdownx/", include(markdownx_urls)),
    path("users/", include("users.urls", namespace="users")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("", include('cms.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
