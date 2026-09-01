from rest_framework import serializers
from .models import Project, Task


class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = ['id','name','project_owner','workspace','created_at']
        read_only_fields = ['workspace', 'project_owner']
class TaskSerializer(serializers.Serializer):
    
    class Meta:
        model = Task
        fields = ['title','description','project','status','assignee','created_at','updated_at']
        read_only_fields = ['workspace']

    