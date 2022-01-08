from django.contrib import admin
from django.contrib.auth import models
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Товары"""
    list_display = ('name', 'category', 'price', 'created',)
