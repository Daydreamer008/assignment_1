from django.db import models
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class Resident(models.Model):
    resident_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_id = models.EmailField()
    resident_building_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("view_resident_name", "Can view resident name"),
            ("change_resident_name", "Can change resident name"),
            ("delete_resident_name", "Can delete resident name"),
        ]

class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    employee_contact_number = models.CharField(max_length=20)
    employee_email_id = models.EmailField()
    assigned_groups = models.ManyToManyField(Group)

    class Meta:
        permissions = [
            ("view_employee_name", "Can view employee name"),
            ("change_employee_name", "Can change employee name"),
            ("delete_employee_name", "Can delete employee name"),
        ]

class CommunityEvent(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_description = models.TextField()

    class Meta:
        permissions = [
            ("view_event_name", "Can view event name"),
            ("change_event_name", "Can change event name"),
            ("delete_event_name", "Can delete event name"),
        ]

resident_manager_group, _ = Group.objects.get_or_create(name='Resident Manager')
operations_manager_group, _ = Group.objects.get_or_create(name='Operations Manager')
sales_executive_group, _ = Group.objects.get_or_create(name='Sales Executive')
community_manager_group, _ = Group.objects.get_or_create(name='Community Manager')
