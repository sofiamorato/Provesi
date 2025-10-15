from django.urls import path
from . import views

app_name = "inventory"  # Cambiar "measurements" a "inventory"

urlpatterns = [
    path("", views.home, name="home"),
    path("scan/", views.scan_api, name="scan_api"),
    path("metrics/", views.metrics, name="metrics"),
]
