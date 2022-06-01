from cgi import test
from email.policy import HTTP
import imp
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound
from projects.models import Projects
from projects.serializers import ProjectsSerializer
from users.models import Users
class ProjectViews(generics.ListCreateAPIView):
    serializer_class = ProjectsSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)

    def get_queryset(self):
            return Projects.objects.filter(user=self.request.user.id)
