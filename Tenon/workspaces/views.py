from rest_framework import viewsets
from .models import Workspace
class TenantModelViewSet(viewsets.ModelViewSet):
    def get_workspace_id(self):
        return self.request.META.get('HTTP_X_WORKSPACE_ID')

    def get_queryset(self):
        workspace_id = self.get_workspace_id()
        if not workspace_id:
            return self.queryset.model.objects.none()
        return self.queryset.filter(workspace_id=workspace_id)
    def perform_create(self,serializer,**kwargs):
        serializer.save(
            workspace_id=self.get_workspace_id(),
            **kwargs)