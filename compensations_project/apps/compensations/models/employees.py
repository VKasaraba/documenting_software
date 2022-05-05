from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from datetime import date
from compensations_project.apps.compensations.managers.employee_manager import EmployeeManager


class Company(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=120)
    rating = models.IntegerField()
    employees_number = models.IntegerField()


class Employee(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=180, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    payment_rate = models.FloatField()
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = EmployeeManager()

    def save(self, *args, **kwargs):
        raw_password = self.password
        self.set_password(raw_password)
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_email(self):
        return self.email

    def get_days_in_company(self, user):
        if user.id == self.id or user.is_manager:
            return (date.today - self.date_joined).days
        else:
            raise PermissionError

    def get_payment_rate(self, user):
        if user.id == self.id or user.is_manager:
            return self.payment_rate
        else:
            raise PermissionError

    def do_work(self):
        print('Working...')
        return True
