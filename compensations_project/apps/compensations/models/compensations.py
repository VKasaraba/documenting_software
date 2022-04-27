from django.db import models
from compensations_project.apps.compensations.models.projects import Task


class CompensationType(models.TextChoices):
    BONUS = 'bonus'
    MEDICAL = 'medical'
    EDUCATIONAL = 'educational'
    SPORT = 'sport'
    OVERTIME = 'overtime'


class CompensationStatus(models.TextChoices):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'


class BonusCompensation(models.Model):
    requested_compensation = models.FloatField()
    reason = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    contact_person = models.CharField(max_length=50)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class MedicalCompensation(models.Model):
    requested_compensation = models.FloatField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    hospital = models.CharField(max_length=50)
    medical_statement_url = models.CharField(max_length=200)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class EducationalCompensation(models.Model):
    requested_compensation = models.FloatField()
    institution = models.CharField(max_length=50)
    issue_date = models.DateTimeField()
    course_name = models.CharField(max_length=50)
    certificate_url = models.CharField(max_length=200)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class SportCompensation(models.Model):
    requested_compensation = models.FloatField()
    gym = models.CharField(max_length=50)
    receipt_url = models.CharField(max_length=200)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class OvertimeWorkCompensation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    hours_amount = models.FloatField()

    def _get_requested_money(self, employee):
        return self.hours_amount * employee.get_payment_rate(employee) * 1.2


COMPENSATION_TYPE_DICT = {
    CompensationType.BONUS: BonusCompensation,
    CompensationType.MEDICAL: MedicalCompensation,
    CompensationType.EDUCATIONAL: EducationalCompensation,
    CompensationType.SPORT: SportCompensation,
    CompensationType.OVERTIME: OvertimeWorkCompensation,
}


class CompensationRequest(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    compensation_type = models.CharField(max_length=30, choices=CompensationType.choices)
    compensation_info_id = models.IntegerField(null=True)
    status = models.CharField(max_length=30, choices=CompensationStatus.choices, default=CompensationStatus.PENDING)

    def get_employee(self):
        return self.employee

    def get_compensation_info_obj(self, user):
        if user.id == self.get_employee().id or user.is_manager:
            info_id = self.compensation_info_id
            info_model = COMPENSATION_TYPE_DICT[self.compensation_type]
            info_obj = info_model.objects.get(id=info_id)
            return info_obj
        else:
            raise PermissionError

    def get_requested_money(self, user):
        if user.id == self.get_employee().id or user.is_manager:
            compensation_obj = self.get_compensation_info_obj(user)
            return compensation_obj._get_requested_money(employee=self.get_employee())
        else:
            raise PermissionError