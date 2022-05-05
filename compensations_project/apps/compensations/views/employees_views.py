from django.shortcuts import render
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from compensations_project.apps.compensations.models.employees import Employee
from compensations_project.apps.compensations.serializers.employees_serializers import EmployeeSerializer


class EmployeeListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        result_qs = Employee.objects.none()
        for person in Employee.objects.all():
            if not person.is_manager:
                result_qs = result_qs.union(Employee.objects.filter(id=person.id))
        return result_qs


class EmployeeRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        result_qs = Employee.objects.none()
        for person in Employee.objects.all():
            if not person.is_manager:
                result_qs = result_qs.union(Employee.objects.filter(id=person.id))
        return result_qs


class FinancialManagerListCreateAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        result_qs = Employee.objects.none()
        for person in Employee.objects.all():
            if person.is_manager:
                result_qs = result_qs.union(Employee.objects.filter(id=person.id))
        return result_qs


class FinancialManagerRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        result_qs = Employee.objects.none()
        for person in Employee.objects.all():
            if person.is_manager:
                result_qs = result_qs.union(Employee.objects.filter(id=person.id))
        return result_qs