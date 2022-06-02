from django.db import models
import uuid

from tickets.models import Tickets
from users.models import Users


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Tickets, on_delete=models.RESTRICT)
    user = models.ForeignKey(Users, on_delete=models.RESTRICT)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    content = models.CharField(max_length=255)
