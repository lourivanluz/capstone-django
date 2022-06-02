from typing import Tuple
from django.db import models
import uuid
import tickets


from users.models import Users


SEVERITY_CHOICES = [("low", "Low"), ("moderate", "Moderate"), ("critical", "Critical")]

CATEGORY_CHOICES = [
    ("flaw", "Flaw"),
    ("improvemente", "Improvemente"),
    ("suggestion", "Suggestion"),
]


FREQUENCY_CHOICES = [
    ("Constact", "Constact"),
    ("Periodic", "Periodic"),
    ("Irreproducible", "Irreproducible"),
]

STATUS_CHOICES = [
    ("reported", "Reported"),
    ("irrelevant", "Irrelevant"),
    ("admitted", "Admitted"),
    ("assignet", "Assignet"),
    ("done", "Done"),
    ("returned", "Returned"),
    ("resolved", "Resolved"),
]


class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    users = models.ManyToManyField(Users, related_name="projects")


class Tickets(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, null=False)
    description = models.TextField(blank=False, null=False)
    test_steps = models.CharField(max_length=255, null=False)
    severity = models.CharField(max_length=255, choices=SEVERITY_CHOICES, null=False)
    frequency = models.CharField(max_length=255, choices=FREQUENCY_CHOICES, null=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, null=False)
    deadline = models.DateField(default="2020-03-15")

    project = models.ForeignKey(
        "tickets.Projects", on_delete=models.CASCADE, related_name="tickets", null=True
    )
    author = models.ForeignKey(
        "users.Users", on_delete=models.CASCADE, related_name="tickets_owner", null=True
    )

    responsibles = models.ManyToManyField(
        "users.Users",
        related_name="tickets",
    )
