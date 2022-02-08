from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user"""
    phone = models.CharField("Mobile phone", max_length=16, blank=True)
    birth_date = models.DateField("Date of birth", null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
