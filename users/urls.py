from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view()),   
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('user', UserView.as_view()),
    path('download', download_file),
    path('jointeam', JoinTeam.as_view()),
    path('leaveteam', LeaveTeam.as_view()),
]