from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound

from projects.models import Projects
from projects.permissions import IsInProject
from projects.serializers import AddProjectUserSerializer, ProjectsSerializer

class ProjectViews(generics.ListCreateAPIView):
    serializer_class = ProjectsSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(users=[self.request.user])

    def get_queryset(self):
            return Projects.objects.filter(users=self.request.user.id)

class AddProjectUserView(APIView):
    serializer_class = AddProjectUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInProject]
    
    def post(self, request, project_id):
        try:
            serializer = self.serializer_class(data=request.data)

            user = serializer.validate_user()
            project = Projects.objects.filter(id=project_id).get()

            project.users.add(user)

            return Response({"message": f"{user.username} was added to {project.title}"}, 200)

        except ValidationError as e:
            return Response(e.detail, e.status_code)
        
        except NotFound as e:
            return Response({"detail": e.detail}, e.status_code)