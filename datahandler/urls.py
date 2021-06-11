from django.urls import path
from .views import IncomingData

urlpatterns = [
    path('upload', IncomingData.as_view()),
]