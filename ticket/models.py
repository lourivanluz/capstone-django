from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

""" from django.url import reverse """

PRIORITY_CHOICES = (
    ("critical", "Critical"),
    ("major", "Major"),
    ("medium", "Medium"),
    ("minor", "Minor"),
    ("trivial", "Trivial"),
)
TYPE_CHOICES = (("bug", "Bug"), ("feature", "Feature"))


class Ticket(models.Model):

    title = models.CharField(max_length=64, defaut=False)
    description = models.TextField(blank=False)
    priority = models.CharField(
        max_length=8, choices=PRIORITY_CHOICES, defaut="trivial"
    )
    ticket_type = models.CharField(max_length=7, choices=TYPE_CHOICES, defaut="bug")
    date_added = models.DateTimeField(defaut=timezone.now, blank=False, editable=False)
    created_by = models.CharField(
        max_length=32, defaut=" ", blank=False, editable=False
    )

    def __str__(self):
        return self.title


""" class Comment(models.Model):
    ticket = models.ForeignKey('tickets.Ticket', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=32)
    text = models.CharField(max_length=512)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text """
