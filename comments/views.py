from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotFound

from comments.models import Comments
from comments.serializers import CommentsSerializer
from tickets.models import Tickets

class CommentsView(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        try:
            ticket_id = self.kwargs['ticket_id']
            ticket = Tickets.objects.filter(id=ticket_id).get()
        except:
            raise NotFound
        serializer.save(ticket=ticket, user=self.request.user)

    def get_queryset(self):
        ticket_id = self.kwargs['ticket_id']
        try:
            return Comments.objects.filter(ticket_id=ticket_id)
        except:
            raise NotFound
