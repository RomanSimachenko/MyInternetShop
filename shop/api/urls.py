from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('products/', views.getProducts),
    path('products/<int:pk>/', views.getProduct),

    path('categories/', views.getCategories),

    path('brands/', views.getBrands),

    path('reviews/<int:pk>/', views.getReviews),

    path('recommended-products/', views.getRecommendedProducts),
]
