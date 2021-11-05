from django.urls import path
from . import views  # Use this for functions
from .views import CreateUser  # Use this for classes
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path("create", CreateUser.as_view(), name="create"),
    path("login", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
