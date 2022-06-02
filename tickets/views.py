from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError, NotFound

from tickets.serializers import (
    AssignTicketUserSerializer,
    TicketSerializer,
    TicketAddSerializer,
    TicketPatchSerializer,
)
from projects.models import Projects
from tickets.models import Tickets
from projects.permissions import IsInProject


class TicketView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInProject]
    queryset = Tickets.objects
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        try:
            project_id = self.kwargs["project_id"]
            project: Projects = Projects.objects.filter(id=project_id).get()
            project.users.filter(id=self.request.user.id).get()

        except:
            raise NotFound
        serializer.save(author=self.request.user, project=project)

    def get_queryset(self):
        project_id = self.kwargs["project_id"]
        try:
            return Tickets.objects.filter(project_id=project_id)
        except:
            raise NotFound


class TicketAddView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInProject]

    def post(self, request, project_id, ticket_id):
        try:
            serializer = AssignTicketUserSerializer(data=request.data)

            user = serializer.validate_user_project(project_id)
            ticket = serializer.validate_ticket(ticket_id)

            ticket.assigned.add(user)

            return Response({"message": f"{user.username} was added to ticket {ticket.id}"}, 200)

        except ValidationError as e:
            return Response(e.detail, e.status_code)
        
        except NotFound as e:
            return Response({"detail": e.detail}, e.status_code)

    def patch(self, request: Request, **kwargs):
        serializer = TicketPatchSerializer(data=request.data)
        serializer.is_valid(True)
        try:
            ticket = Tickets.objects.filter(id=kwargs["ticket_id"])

        except:
            return Response({"error": "notfound"})
        ticket.update(**serializer.validated_data)

        serializer = TicketAddSerializer(ticket.first())
        return Response(serializer.data, 200)
