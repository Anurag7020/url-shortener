from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortenerAPIView.as_view(), name='create-short-url'),
    path('<str:code>/',views.URLHitAPIView.as_view(),name='redirect'),
]
