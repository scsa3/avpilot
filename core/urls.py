from django.urls import path
from . import views

urlpatterns = [
    path('stream/', views.stream_mp4, name='stream_mp4'),
]
