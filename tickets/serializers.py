from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from projects.models import Projects
from tickets.models import Tickets
from users.models import Users
from users.serializers import UsersSerializer


class TicketSerializer(serializers.ModelSerializer):
    assigned = UsersSerializer(read_only=True, many=True)
    author = UsersSerializer(read_only=True)

    class Meta:
        model = Tickets
        fields = (
            "id",
            "author",
            "category",
            "description",
            "test_steps",
            "severity",
            "frequency",
            "status",
            "deadline",
            "assigned",
        )
        read_only_fields = (
            "id",
            "deadline",
        )

class AssignTicketUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_user_project(self, project_id):
        self.is_valid(raise_exception=True)
        project = Projects.objects.filter(id=project_id).get()
        try:
            user = Users.objects.filter(email=self.validated_data['email']).get()
            if not user in project.users.all():
                raise ValidationError
        except:
            raise NotFound(detail="user not found")

        return user

    def validate_ticket(self, ticket_id):
        try:
            ticket = Tickets.objects.filter(id=ticket_id).get()
        except:
            raise NotFound(detail="ticket not found")

        return ticket


class TicketPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            "category",
            "description",
            "test_steps",
            "severity",
            "frequency",
            "status",
            "deadline",
        )

        extra_kwargs = {
            "category": {"required": False},
            "description": {"required": False},
            "test_steps": {"required": False},
            "severity": {"required": False},
            "frequency": {"required": False},
            "status": {"required": False},
            "deadline": {"required": False},
        }
