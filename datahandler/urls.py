from django.urls import path
from .views import GetRecordInfo, GetSessionData, IncomingData

urlpatterns = [
    path('upload', IncomingData.as_view()),
    path('record', GetRecordInfo.as_view()),
    path('car', GetSessionData.as_view()),
]