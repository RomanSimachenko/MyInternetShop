from itertools import product
from tabnanny import verbose
from django.db import models
from users.models import CustomUser


class Message(models.Model):
    """Messages"""
    name = models.CharField("Name", max_length=300)
    email = models.EmailField("Email")
    subject = models.CharField("Subject", max_length=200)
    body = models.TextField("Message text")
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Category(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    """Brands"""
    name = models.CharField("Brand", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Product(models.Model):
    """Products"""
    name = models.CharField("Product", max_length=300)
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(
        Brand, verbose_name="Brand", on_delete=models.SET_NULL, null=True)
    image = models.ImageField("Image", null=True, upload_to='shop/images/')
    description = models.TextField("Description", null=True)
    price = models.PositiveIntegerField(
        "Price", help_text="indicate the price in UAH")
    avaible = models.CharField(
        "Availability", default="In stock", max_length=100)
    condition = models.CharField("Condition", default="New", max_length=100)
    quantity = models.PositiveIntegerField("Quantity", default=1)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-added']
        verbose_name = "Product"
        verbose_name_plural = "Products"


class RecommendedProduct(models.Model):
    """Recommended products"""
    product = models.ManyToManyField(
        Product, verbose_name="Recommended products")

    class Meta:
        verbose_name = "Recommended product"
        verbose_name_plural = "Recommended products"


class CartProduct(models.Model):
    """Cart products"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Quantity", default=1)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Cart product"
        verbose_name_plural = "Cart products"


class MailingList(models.Model):
    """Mailing list"""
    email = models.EmailField("Email")

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ('email',)
        verbose_name = "Mailing list"
