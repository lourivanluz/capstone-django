from django.urls import path


from tickets.views import TicketView, TicketAddView

urlpatterns = [
    path("projects/<str:project_id>/tickets", TicketView.as_view()),
    path("projects/<str:project_id>/tickets/<str:ticket_id>/", TicketAddView.as_view()),
]
