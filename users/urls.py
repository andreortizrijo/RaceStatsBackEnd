from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserView, download_file

urlpatterns = [
    path('register', RegisterView.as_view()),   
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),
    path('download', download_file),
]