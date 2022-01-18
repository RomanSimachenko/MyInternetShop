from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', views.errorPage, name='error'),

    path('', views.index, name='home'),

    path('login-register/', views.login_registerPage, name='login-register'),
    path('logout/', views.logoutUser, name='logout'),

    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

    path('product/<int:pk>/', views.product_detail, name='product-detail'),

    path('addCart/<int:pk>/', views.addCart, name='addCart'),
    path('deleteCart/<int:pk>/', views.deleteCart, name='deleteCart'),

    path('changeQuantity/<int:pk>/', views.changeQuantity, name='changeQuantity'),
    path('addQuantity/<int:pk>/', views.addQuantity, name='addQuantity'),
    path('reduceQuantity/<int:pk>/', views.reduceQuantity, name='reduceQuantity'),

    path('addMail/', views.addMail, name='addMail'),

    path('addReview/<int:pk>/', views.addReview, name='addReview'),
    path('deleteReview/<int:pk>/', views.deleteReview, name='deleteReview'),
]
