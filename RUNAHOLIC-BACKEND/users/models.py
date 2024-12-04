from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=250, verbose_name="Nome Completo")

    def __str__(self):
        return self.username