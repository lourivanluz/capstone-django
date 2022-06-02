from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotFound

from tickets.models import Tickets


class IsInTicket(BasePermission):
    def has_permission(self, request, view):
        ticket_id = view.kwargs.get("ticket_id")
        restrict_methods = [
            "PATCH",
        ]
        try:
            ticket: Tickets = Tickets.objects.filter(id=ticket_id).get()
        except:
            raise NotFound(detail="ticket not found")

        if request.method in restrict_methods and (
            request.user in ticket.assigned.all() or request.user.id == ticket.author.id
        ):
            return True
        return False
