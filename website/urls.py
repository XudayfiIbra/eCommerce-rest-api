from django.urls import path
from . import views


urlpatterns = [
    path('api-products', views.api_products, name="api_products"),
    path('api-products/<int:id>/', views.api_products_info, name="api_products_info"),
    path('api-customers/', views.api_customers, name='api_customers'),
    path('api-customers/<int:id>/', views.api_customers_info, name="api_customer_info"),
    path('api-branches/', views.api_branches, name='api_branches'),
    path('api-branches/<int:id>/', views.api_branches_info, name='api_branches_info'),
    path('api-employees/', views.api_employees, name='api_employees'),
    path('api-employees/<int:id>/', views.api_employees_info, name='api_employees_info'),
    # path('products', views.search, name="product_search")
]
