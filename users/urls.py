from rest_framework.urls import path


from users.views import UserView, loguin

urlpatterns = [
    path("register/", UserView.as_view()),
    path("login/", loguin),
]
