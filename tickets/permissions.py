from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class isMember(BasePermission):
    def has_permission(self, request: Request, _):
        restrict_methods = [
            "POST",
        ]
        if request.method in restrict_methods and request.user.is_anonymous:
            return False
        return True
