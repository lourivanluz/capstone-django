from rest_framework.permissions import BasePermission
from rest_framework.exceptions import NotFound

from projects.models import Projects

class IsInProject(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_id')

        try:
            project = Projects.objects.filter(id=project_id).get()
        except:
            raise NotFound(detail="project not found")

        return request.user in project.users.all()