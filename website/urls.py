from django.urls import path
from . import views


urlpatterns = [
    path('api-products/', views.api_products, name="api_products"),
    path('api-products/<int:id>', views.api_products_info, name="api_products_info")
]
