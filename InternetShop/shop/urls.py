from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', views.adminPage),

    path('', views.index, name='home'),
]
