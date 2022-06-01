from rest_framework import serializers

from projects.models import Projects
from users.serializers import UsersSerializer

class ProjectsSerializer(serializers.ModelSerializer):
    user = UsersSerializer(read_only=True)

    class Meta:
        model = Projects
        fields = ('id', 'title', 'description','user')