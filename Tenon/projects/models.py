from django.db import models
from django.conf import settings
from workspaces.models import Workspace

class TenantAwareModel(models.Model):
    """
    Any model that inherits from this model shall be tied to a workspace.
    """
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    class Meta:
        abstract = True
        


class Project(TenantAwareModel):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    project_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    def __str__(self):
        return f"{self.name} ({self.workspace.name})"
    
class Task(TenantAwareModel):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('REVIEW', 'In Review'),
        ('DONE', 'Done')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='assigned_tasks',null=True,blank=True    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"