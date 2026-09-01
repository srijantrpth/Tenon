from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.response import Response
from workspaces.views import TenantModelViewSet

class ProjectViewSet(TenantModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        super().perform_create(
            serializer=serializer,
            project_owner = self.request.user
        )
class TaskViewSet(TenantModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def perform_create(self,serializer):
        super().perform_create(
            serializer=serializer,
            assignee=self.request.user,
            
        )
