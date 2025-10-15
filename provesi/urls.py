# provesi/urls.py
from django.contrib import admin
from django.urls import path, include
from inventory.views import home  # <-- agrega esta línea

# ...existing code...

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inventory/", include("inventory.urls", namespace="inventory")),
    path("products/", include("products.urls", namespace="products")),  # <-- agrega esta línea
    path("", home, name="home"),
]
