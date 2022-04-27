from rest_framework import serializers
from compensations_project.apps.compensations.models.employees import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        write_only_fields = ('password', )
