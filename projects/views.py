from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from projects.models import Projects
from projects.serializers import ProjectsSerializer

class ProjectViews(generics.ListCreateAPIView):
    serializer_class = ProjectsSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    def get_queryset(self):
            return Projects.objects.filter(users=self.request.user.id)
