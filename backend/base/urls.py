from django.urls import path
from . import views

urlpatterns = [
    path("recommend/<str:title>", views.recommend, name="recommend"),
    path("get_all_movies", views.get_all_movies, name="get_all_movies"),
]
