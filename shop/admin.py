from django.contrib import admin
from .models import Category, Brand, Product, RecommendedProduct, Message, MailingList, Review


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Messages"""
    list_display = ('user', 'email', 'subject', 'added',)
    readonly_fields = ('user', 'email', 'subject', 'body', 'added',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Categories"""
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Brands"""
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Products"""
    list_display = ('name', 'category', 'brand', 'price',
                    'avaible', 'condition', 'quantity', 'added',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Review"""
    list_display = ('user', 'product', 'email', 'added',)
    readonly_fields = ('user', 'product', 'email', 'body', 'added',)


@admin.register(RecommendedProduct)
class RecommendedProductAdmin(admin.ModelAdmin):
    """Recommended products"""


# @admin.register(CartProduct)
# class CartProductAdmin(admin.ModelAdmin):
#     """CartProduct"""
#     list_display = ('user', 'product', 'quantity',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    """Mailing list"""
    list_display = ('email',)
    readonly_fields = ('email',)
