# from compensations_project.apps.compensations.models.employees import Employee
from random import randint
import csv


COMPENSATION_TYPES = ['bonus', 'medical', 'educational', 'sport', 'overtime']
BONUS_REASONS = ['Event organizations', 'Tech support', 'Mentoring']
BONUS_CONTACT_PERSONS = ['Mykola Ivankiv', 'Roman Nykolyn', 'Oleg Elechko']
OVERTIME_TASKS = [8, 9, 10, 11, 12]
SPORT_GYMS = ['Malibu', 'Sport_Life', 'Champion']
HOSPITALS = ['Lviv Hospital N5', 'Ternopil Regional Hospital', 'Kyiv Hospital N1']
INTSITUTIONS = ['Standford University', 'Lviv Polytechnic National University', 'Oxford University']


def generate_compensation_requests():
    # employee_ids = Employee.objects.filter(is_manager=False).values_list('id', flat=True
    employee_ids = [4, 5, 7]
    with open('sample_data.csv', 'w') as f:
        writer = csv.writer(f)
        for i in range(round(100/4)):
            # BONUS
            request_data = []
            request_data.append('bonus')
            employee = employee_ids[randint(0, len(employee_ids)-1)]
            request_data.append(employee)
            date_created = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(date_created)
            requested_compensation = randint(10, 100)
            request_data.append(requested_compensation)
            reason = BONUS_REASONS[randint(0, 2)]
            request_data.append(reason)
            date = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(date)
            contact_person = BONUS_CONTACT_PERSONS[randint(0, 2)]
            request_data.append(contact_person)
            bonus_url = f'https://bonus-info'
            request_data.append(bonus_url)
            writer.writerow(request_data)

            # SPORT
            request_data = []
            request_data.append('sport')
            employee = employee_ids[randint(0, len(employee_ids)-1)]
            request_data.append(employee)
            date_created = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(date_created)
            requested_compensation = randint(10, 50)
            request_data.append(requested_compensation)
            gym = SPORT_GYMS[randint(0, len(SPORT_GYMS)-1)]
            request_data.append(gym)
            receipt_url = f'https://{gym.lower()}-receipt'
            request_data.append(receipt_url)
            writer.writerow(request_data)

            # MEDICAL
            request_data = []
            request_data.append('medical')
            employee = employee_ids[randint(0, len(employee_ids)-1)]
            request_data.append(employee)
            date_created = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(date_created)
            requested_compensation = randint(10, 50)
            request_data.append(requested_compensation)
            start_date = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(start_date)
            end_date = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(end_date)
            hospital = HOSPITALS[randint(0, len(HOSPITALS)-1)]
            request_data.append(hospital)
            medical_statement_url = f'https://medical_statement'
            request_data.append(medical_statement_url)
            writer.writerow(request_data)

            # EDUCATIONAL
            request_data = []
            request_data.append('educational')
            employee = employee_ids[randint(0, len(employee_ids)-1)]
            request_data.append(employee)
            date_created = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(date_created)
            requested_compensation = randint(10, 50)
            request_data.append(requested_compensation)
            institution = INTSITUTIONS[randint(0, len(INTSITUTIONS)-1)]
            request_data.append(institution)
            issue_date = f'202{randint(0, 2)}-0{randint(1, 9)}-0{randint(1, 9)}'
            request_data.append(issue_date)
            course_name = 'Programming Course'
            request_data.append(course_name)
            certificate_url = f'https://certificate'
            request_data.append(certificate_url)
            writer.writerow(request_data)


generate_compensation_requests()