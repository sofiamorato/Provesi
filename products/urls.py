from django.urls import path
from .views import register_product_page, register_product_api

app_name = "products"

urlpatterns = [
    path("register/", register_product_page, name="register_page"),
    path("register/api/", register_product_api, name="register_api"),
]