from django.urls import path, include
from rest_framework.routers import DefaultRouter

from planetarium.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    PlanetariumDomeViewSet,
)

router = DefaultRouter()
router.register(r"astronomy-shows", AstronomyShowViewSet)
router.register(r"show-themes", ShowThemeViewSet)
router.register(r"show-sessions", ShowSessionViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"planetarium-domes", PlanetariumDomeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "planetarium"
