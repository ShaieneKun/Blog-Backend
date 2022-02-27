from django.contrib import admin
from django.urls import path, include

# from markdownx import urls as markdownx_urls
from rest_framework import routers
import debug_toolbar
from blog import views

import debug_toolbar
from main import settings

# REST framework's paths
rest_router = routers.DefaultRouter()
rest_router.register("articles", views.ArticleSerializedView, "articles")

urlpatterns = [
    path("", include("index.urls", namespace="index")),
    path("admin/", admin.site.urls),
    path("api/", include(rest_router.urls)),
    path("old-blog/", include("blog.urls", namespace="old-blog")),
    # path("markdownx/", include(markdownx_urls)),
    path("users/", include("users.urls", namespace="users")),
    path(r"^ckeditor/", include("ckeditor_uploader.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
    path("blog/", include('cms.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
