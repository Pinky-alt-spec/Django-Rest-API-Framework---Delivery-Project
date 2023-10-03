from django.urls import path
from . import views


urlpatterns = [
    path('', views.AuthView.as_view(), name="Hello world"),
    path('signup/', views.UserCreateView.as_view(), name="sign_up")
]