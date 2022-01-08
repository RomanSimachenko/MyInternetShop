from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Товары"""
    name = models.CharField("Товар", max_length=300)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=SET_NULL, null=True)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField(
        "Цена", default=0, help_text="указывать сумму в гривнах")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
