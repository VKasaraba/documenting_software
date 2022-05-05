"""compensations_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import truediv
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path
from compensations_project.apps.compensations.models.compensations import CompensationRequest
from compensations_project.apps.compensations.models.employees import Employee
from compensations_project.apps.compensations.serializers.compensations_serializers import CompensationRequestSerializer
from compensations_project.apps.compensations.views.compensation_views import CompensationRequestListCreateAPIView, CompensationRequestRetrieveUpdateAPIView, UploadCompensationCSVFile
from compensations_project.apps.compensations.views.employees_views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateAPIView, FinancialManagerListCreateAPIView, FinancialManagerRetrieveUpdateAPIView
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.backends import TokenBackend
from compensations_project.apps.compensations.views.projects_views import ProjectListCreateAPIView, ProjectRetrieveUpdateAPIView, TaskListCreateAPIView, TaskRetrieveUpdateAPIView


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('employees/', EmployeeListCreateAPIView.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateAPIView.as_view()),

    path('financial_managers/', FinancialManagerListCreateAPIView.as_view()),
    path('financial_managers/<int:pk>/', FinancialManagerRetrieveUpdateAPIView.as_view()),

    path('compensation_requests/', CompensationRequestListCreateAPIView.as_view()),
    path('compensation_requests/<int:pk>/', CompensationRequestRetrieveUpdateAPIView.as_view()),

    path('projects/', ProjectListCreateAPIView.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateAPIView.as_view()),

    path('tasks/', TaskListCreateAPIView.as_view()),
    path('tasks/<int:pk>/', TaskRetrieveUpdateAPIView.as_view()),

    path('upload_csv/', UploadCompensationCSVFile.as_view()),
]
