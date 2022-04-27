from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from compensations_project.apps.compensations.models.projects import Project, Task
from compensations_project.apps.compensations.serializers.projects_serializers import ProjectSerializer, TaskSerializer


class ProjectListCreateAPIView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        project_id = request.data.pop('project')
        created_response = super().create(request, *args, **kwargs)
        task_obj = Task.objects.get(id=created_response.data.get('id'))
        project_obj = Project.objects.get(id=project_id)
        task_obj.set_project(project_obj)       # INTERFACE INJECTION
        return created_response


class TaskRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()