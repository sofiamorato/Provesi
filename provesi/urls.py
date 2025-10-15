# provesi/urls.py
from django.contrib import admin
from django.urls import path, include
from inventory.views import home  
from django.http import JsonResponse

# ...existing code...

def health_check(request):
    return JsonResponse({"status": "healthy"}, status=200)
    return JsonResponse({"status": "healthy"}, status=200)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inventory/", include("inventory.urls", namespace="inventory")),
    path("products/", include("products.urls", namespace="products")),  
    path("", home, name="home"),
    path("health-check/", health_check, name="health_check"),  
]
