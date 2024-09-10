from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    MovieSessionViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("genres", GenreViewSet, basename="genres")
router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-halls"
)
router.register(
    "movie_sessions",
    MovieSessionViewSet,
    basename="movie-sessions"
)
router.register("actors", ActorViewSet, basename="actors")

urlpatterns = [
    path(router.register("movies", MovieViewSet, basename="movies")),
    path(router.register("genres", GenreViewSet, basename="genres")),
    path(router.register(
        "cinema_halls",
        CinemaHallViewSet,
        basename="cinema-halls"
    )),
    path(router.register(
        "movie_sessions",
        MovieSessionViewSet,
        basename="movie-sessions"
    )),
    path(router.register("actors", ActorViewSet, basename="actors")),
]
