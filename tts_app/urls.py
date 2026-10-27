from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo_tts, name='demo_tts'),
    path('convert/', views.convert_tts, name='convert_tts'),
]