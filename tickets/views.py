from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound


from tickets.serializers import ProjectSerializer, TicketSerializer, TicketAddSerializer
from users.models import Users
from tickets.models import Projects, Tickets
from tickets.permissions import isMember


class TicketView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isMember]
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
    def post(self, request: Request, **kwargs):

        serializer = TicketAddSerializer(data=request.data)
        # serializer.is_valid(True)

        try:
            ticket: Tickets = Tickets.objects.filter(id=kwargs["ticket_id"]).get()

        except:
            return Response({"error": "notfound"})
        ticket.responsibles.add(request.data["responsibles"])
        ticket.save()
        serializer = TicketAddSerializer(ticket)
        return Response(serializer.data, HTTP_201_CREATED)


""" class TicketGetView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isMember]
    queryset = Tickets.objects
    serializer_class = TicketSerializer

    def get(self, request: Request, *args, **kwargs):
        self.queryset = request.user.tickets.all()
        return super().get(request, *args, **kwargs) """


class ProjectView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = []
    queryset = Projects.objects.all
    serializer_class = ProjectSerializer

    def create(self, request: Request):
        user: Users = request.user

        serialiser = ProjectSerializer(data=request.data)
        serialiser.is_valid(raise_exception=True)

        project: Projects = Projects.objects.create(**serialiser.validated_data)
        project.users.add(user)
        project.save()
        serialiser = ProjectSerializer(project)

        return Response(serialiser.data, HTTP_201_CREATED)
