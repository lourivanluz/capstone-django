from statistics import mode
from django.db import models
from uuid import uuid4
from users.models import Users
# Create your models here.
class Projects (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title=models.CharField(max_length=255,unique=True)
    description=models.CharField(max_length=1023)
    user = models.ForeignKey(Users, on_delete=models.RESTRICT,related_name="projects")