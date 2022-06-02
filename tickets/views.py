from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound


from tickets.serializers import (
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

    def post(self, request: Request, **kwargs):

        serializer = TicketAddSerializer(data=request.data)
        # serializer.is_valid(True)

        try:
            ticket: Tickets = Tickets.objects.filter(id=kwargs["ticket_id"]).get()

        except:
            return Response({"error": "ticket not found"})
        ticket.assigned.add(request.data["assigned"])
        ticket.save()
        serializer = TicketAddSerializer(ticket)
        return Response(serializer.data, HTTP_201_CREATED)

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
