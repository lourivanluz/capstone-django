from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    username = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
