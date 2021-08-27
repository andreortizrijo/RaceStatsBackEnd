from django.urls import path
from .views import *

urlpatterns = [
    path('upload-car', CarData.as_view()),
    path('upload-track', TrackData.as_view()),
    path('upload-time', TimeData.as_view()),
    path('upload-session', RegisterSession.as_view()),
    path('record', GetRecordInfo.as_view()),
    path('live', Live.as_view())
]