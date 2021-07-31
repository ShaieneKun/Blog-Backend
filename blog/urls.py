from django.urls import path, include
from django.contrib.auth.views import LoginView
from rest_framework import routers
from .views import PostViewSet, PostsView, ArticleView, NewPostView, UpdatePostView, DeletePostView # Use this for classes
from . import views # Use this for functions

app_name = 'blog'

router = routers.DefaultRouter()

router.register(r'api', PostViewSet)

urlpatterns = [ 
    # path('', PostsView.as_view(), name = "posts"),
    # path('article/<int:pk>', ArticleView.as_view(), name='articleDetail'),
    # path('article/<int:pk>/update', UpdatePostView.as_view(), name='articleUpdate'),
    # path('article/<int:pk>/delete', DeletePostView.as_view(), name='articleDelete'),
    # path('postForm', NewPostView.as_view(), name='postForm'),
    # path('accounts/login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
	path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
]