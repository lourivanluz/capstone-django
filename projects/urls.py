from django.urls import path

from projects.views import AddProjectUserView, ProjectViews

urlpatterns = [
    path('projects/', ProjectViews.as_view()),
    path('projects/<str:project_id>/', AddProjectUserView.as_view())
]