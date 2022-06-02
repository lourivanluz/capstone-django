from django.urls import path


from tickets.views import TicketView, TicketAddView

urlpatterns = [
    path("ticket/project/<str:project_id>/", TicketView.as_view()),
    path("ticket/user/<str:ticket_id>/", TicketAddView.as_view()),
]
