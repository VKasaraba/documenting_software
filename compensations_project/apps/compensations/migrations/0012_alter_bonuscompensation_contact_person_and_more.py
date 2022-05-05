# Generated by Django 4.0.4 on 2022-05-03 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compensations', '0011_rename_certificate_url_educationalcompensation_proof_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscompensation',
            name='contact_person',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bonuscompensation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bonuscompensation',
            name='proof_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bonuscompensation',
            name='reason',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bonuscompensation',
            name='requested_compensation',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='compensationrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='educationalcompensation',
            name='course_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='educationalcompensation',
            name='institution',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='educationalcompensation',
            name='issue_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='educationalcompensation',
            name='proof_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalcompensation',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='medicalcompensation',
            name='hospital',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='medicalcompensation',
            name='proof_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalcompensation',
            name='requested_compensation',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='medicalcompensation',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='overtimeworkcompensation',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compensations.task'),
        ),
        migrations.AlterField(
            model_name='sportcompensation',
            name='gym',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sportcompensation',
            name='proof_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
