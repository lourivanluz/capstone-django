from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotFound

from tickets.models import Tickets

class IsInTicket(BasePermission):
    def has_permission(self, request, view):
        ticket_id = view.kwargs.get('ticket_id')

        try:
            ticket = Tickets.objects.filter(id=ticket_id).get()
        except:
            raise NotFound(detail="ticket not found")

        return request.user in ticket.assigned.all()