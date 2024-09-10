from django.urls import path, include
from rest_framework import routers

from cinema import views

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")
router.register("genres", views.GenreViewSet, basename="genres")
router.register(
    "cinema_halls",
    views.CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movie_session",
    views.MovieSessionViewSet,
    basename="movie_session"
)
router.register("actors", views.ActorViewSet, basename="actors")

urlpatterns = [
    path("", include(router.urls)),
]
