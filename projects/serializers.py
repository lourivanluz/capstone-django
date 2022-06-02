from rest_framework import serializers

from projects.models import Projects
from users.models import Users
from rest_framework.exceptions import NotFound

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title', 'description')

class AddProjectUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_user(self):
        self.is_valid(raise_exception=True)
        try:
            user = Users.objects.filter(email=self.validated_data['email']).get()
        except:
            raise NotFound(detail="user not found")
        return user

    def validate_project(self, project_id):
        try:
            project = Projects.objects.filter(id=project_id).get()
        except:
            raise NotFound(detail="project not found")
        return project