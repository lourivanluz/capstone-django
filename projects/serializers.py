from rest_framework import serializers

from users.serializers import UsersSerializer
from projects.models import Projects
from users.models import Users
from rest_framework.exceptions import NotFound


class ProjectsSerializer(serializers.ModelSerializer):
    users = UsersSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'title', 'description', 'users')

class AddProjectUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_user(self):
        self.is_valid(raise_exception=True)
        try:
            user = Users.objects.filter(email=self.validated_data['email']).get()
        except:
            raise NotFound(detail="user not found")
        return user