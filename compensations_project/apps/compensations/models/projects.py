from statistics import mode
from django.db import models

from compensations_project.apps.compensations.models.employees import Employee


class Project(models.Model):
    repository_url = models.CharField(max_length=120)


class Task(models.Model):
    name = models.CharField(max_length=30, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, default='in progress')
    asigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def set_project(self, project):
        self.project = project
        return True