from django.contrib import admin

from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'project_owner')
    list_filter = ('workspace',)
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','assignee','project', 'status')
    list_filter = ('status','project__workspace')
    search_fields = ('title',)
