from django.urls import path

from projects.views import ProjectViews

urlpatterns = [
    path('projects/', ProjectViews.as_view())
]