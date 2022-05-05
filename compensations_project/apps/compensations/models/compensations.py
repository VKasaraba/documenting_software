from django.db import models
from compensations_project.apps.compensations.models.employees import Employee
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
    requested_compensation = models.FloatField(null=True)
    reason = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    contact_person = models.CharField(max_length=50, null=True)
    proof_url = models.CharField(max_length=200, null=True)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class MedicalCompensation(models.Model):
    requested_compensation = models.FloatField(null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField(null=True)
    hospital = models.CharField(max_length=50, null=True)
    proof_url = models.CharField(max_length=200, null=True)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class EducationalCompensation(models.Model):
    requested_compensation = models.FloatField()
    institution = models.CharField(max_length=50, null=True)
    issue_date = models.DateTimeField(null=True)
    course_name = models.CharField(max_length=50, null=True)
    proof_url = models.CharField(max_length=200, null=True)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class SportCompensation(models.Model):
    requested_compensation = models.FloatField()
    gym = models.CharField(max_length=50, null=True)
    proof_url = models.CharField(max_length=200, null=True)

    def _get_requested_money(self, *args, **kwargs):
        return self.requested_compensation


class OvertimeWorkCompensation(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    hours_amount = models.FloatField()

    def _get_requested_money(self):
        return self.hours_amount * 12 * 1.2


COMPENSATION_TYPE_DICT = {
    CompensationType.BONUS: BonusCompensation,
    CompensationType.MEDICAL: MedicalCompensation,
    CompensationType.EDUCATIONAL: EducationalCompensation,
    CompensationType.SPORT: SportCompensation,
    CompensationType.OVERTIME: OvertimeWorkCompensation,
}


class CompensationRequest(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True)
    date_created = models.DateField(auto_now_add=True)
    compensation_type = models.CharField(max_length=30, choices=CompensationType.choices)
    compensation_info_id = models.IntegerField(null=True)
    status = models.CharField(max_length=30, choices=CompensationStatus.choices, default=CompensationStatus.PENDING, null=True)
    requested_compensation = models.FloatField(null=True)
    user_name = models.CharField(max_length=100, null=True)
    date_str = models.CharField(max_length=100, null=True)
    proof_url = models.CharField(max_length=100, null=True)

    def get_employee(self):
        return self.employee

    def get_compensation_info_obj(self):
        info_id = self.compensation_info_id
        info_model = COMPENSATION_TYPE_DICT[self.compensation_type]
        info_obj = info_model.objects.get(id=info_id)
        return info_obj

    def get_requested_money(self):
        compensation_obj = self.get_compensation_info_obj()
        return compensation_obj._get_requested_money(employee=self.get_employee())

    def save(self, *args, **kwargs):
        res = super(CompensationRequest, self).save(*args, **kwargs)
        info_obj = self.get_compensation_info_obj()
        self.requested_compensation = round(info_obj._get_requested_money())
        self.user_name = None if not self.employee else self.employee.get_full_name()
        self.date_str = str(self.date_created)
        self.proof_url = info_obj.proof_url
        return res