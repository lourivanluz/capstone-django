from django.urls import path

from comments.views import CommentsView

urlpatterns = [
    path('projects/<str:project_id>/tickets/<str:ticket_id>/comments', CommentsView.as_view())
]