from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, ListCreateAPIView,
)
from compensations_project.apps.compensations.models.compensations import  CompensationRequest
from compensations_project.apps.compensations.models.employees import Employee
from compensations_project.apps.compensations.serializers.compensations_serializers import COMPENSATION_TYPE_SERIALIZER_DICT, CompensationRequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
import csv


class CompensationRequestListCreateAPIView(ListCreateAPIView):
    serializer_class = CompensationRequestSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        compensation_type = self.request.query_params.get('compensation_type')

        user = self.request.user
        if user.is_manager:
            qs = CompensationRequest.objects.all()
        else:
            qs = CompensationRequest.objects.filter(employee=user)
        if compensation_type:
            qs = qs.filter(compensation_type=compensation_type)
        print(f'\ngot {qs.count()} records\n')
        return qs

    def create(self, request, *args, **kwargs):
        request_data = request.data
        employee_id = request_data.get('employee')
        # create compensation info object
        info_serializer_class = COMPENSATION_TYPE_SERIALIZER_DICT[request_data.get('compensation_type')]
        info_serializer = info_serializer_class(data=request_data)
        info_serializer.is_valid(raise_exception=True)
        info_obj = info_serializer.save()
        # create compensation request object
        request_serializer = self.get_serializer(data=request_data)
        request_serializer.is_valid(raise_exception=True)
        request_obj = request_serializer.save()

        set_info_to_request(request_obj, info_obj)                      # METHOD INJECTION
        request_obj.empoloyee = Employee.objects.get(id=employee_id)    # PROPERTY INJECTION
        request_obj.save()
        return Response(request_serializer.data, status=status.HTTP_201_CREATED)


class CompensationRequestRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompensationRequestSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return CompensationRequest.objects.all()


##########################################################
#################### FILE UPLOAD VIEW ####################
##########################################################


class UploadCompensationCSVFile(ListCreateAPIView):
    serializer_class = CompensationRequestSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        file = request.data.get('file')
        file_rows = [row.decode("utf-8") for row in file]   # from bytes to str
        reader = csv.reader(file_rows, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL)
        for splitted_values in reader:
            if splitted_values:
                compensation_type = splitted_values[0]
                request_data = format_data_by_compensation_type(compensation_type, splitted_values)
                create_request_record(request_data)
        return Response('Uploaded', status=status.HTTP_201_CREATED)


def format_data_by_compensation_type(compensation_type, splitted_values):
    request_data = {}
    if compensation_type == 'bonus':
        request_data['compensation_type'] = splitted_values.pop(0)
        request_data['employee'] = splitted_values.pop(0)
        request_data['date_created'] = splitted_values.pop(0)
        request_data['requested_compensation'] = splitted_values.pop(0)
        request_data['reason'] = splitted_values.pop(0)
        request_data['date'] = splitted_values.pop(0)
        request_data['contact_person'] = splitted_values.pop(0)
    if compensation_type == 'overtime':
        request_data['compensation_type'] = splitted_values.pop(0)
        request_data['employee'] = splitted_values.pop(0)
        request_data['date_created'] = splitted_values.pop(0)
        request_data['task'] = splitted_values.pop(0)
        request_data['hours_amount'] = splitted_values.pop(0)
    if compensation_type == 'sport':
        request_data['compensation_type'] = splitted_values.pop(0)
        request_data['employee'] = splitted_values.pop(0)
        request_data['date_created'] = splitted_values.pop(0)
        request_data['requested_compensation'] = splitted_values.pop(0)
        request_data['gym'] = splitted_values.pop(0)
        request_data['receipt_url'] = splitted_values.pop(0)
    if compensation_type == 'medical':
        request_data['compensation_type'] = splitted_values.pop(0)
        request_data['employee'] = splitted_values.pop(0)
        request_data['date_created'] = splitted_values.pop(0)
        request_data['requested_compensation'] = splitted_values.pop(0)
        request_data['start_date'] = splitted_values.pop(0)
        request_data['end_date'] = splitted_values.pop(0)
        request_data['hospital'] = splitted_values.pop(0)
        request_data['medical_statement_url'] = splitted_values.pop(0)
    if compensation_type == 'educational':
        request_data['compensation_type'] = splitted_values.pop(0)
        request_data['employee'] = splitted_values.pop(0)
        request_data['date_created'] = splitted_values.pop(0)
        request_data['requested_compensation'] = splitted_values.pop(0)
        request_data['institution'] = splitted_values.pop(0)
        request_data['issue_date'] = splitted_values.pop(0)
        request_data['course_name'] = splitted_values.pop(0)
        request_data['certificate_url'] = splitted_values.pop(0)
    return request_data


def create_request_record(request_data):
    employee_id = request_data.get('employee')
    # create compensation info object
    info_serializer_class = COMPENSATION_TYPE_SERIALIZER_DICT[request_data['compensation_type']]
    info_serializer = info_serializer_class(data=request_data)
    info_serializer.is_valid(raise_exception=True)
    info_obj = info_serializer.save()
    # create compensation request object
    request_serializer = CompensationRequestSerializer(data=request_data)
    request_serializer.is_valid(raise_exception=True)
    request_obj = request_serializer.save()

    set_info_to_request(request_obj, info_obj)                     # METHOD INJECTION
    request_obj.employee = Employee.objects.get(id=employee_id)    # PROPERTY INJECTION
    request_obj.save()
    return True


def set_info_to_request(request_obj, info_obj):
        request_obj.compensation_info_id = info_obj.id
        request_obj.save()
        return True