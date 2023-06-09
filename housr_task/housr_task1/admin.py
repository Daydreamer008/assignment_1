from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import Resident, Employee, CommunityEvent

# class EmployeeAdmin():
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('employee_name', 'employee_contact_number', 'employee_email_id')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'assigned_groups')}),
#     )
#     filter_horizontal = ('assigned_groups',)

#     list_display = ('employee_name', 'employee_email_id')
#     list_filter = ('assigned_groups',)
#     ordering = ('employee_name',)

#     def get_fieldsets(self, request, obj=None):
#         if not obj:
#             self.fieldsets += (('Groups', {'fields': ('assigned_groups',)}),)
#         return super().get_fieldsets(request, obj)


admin.site.register(Resident)
admin.site.register(Employee)
admin.site.register(CommunityEvent)
admin.site.unregister(Group)
admin.site.register(Group)
admin.site.register(Permission)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin, GroupAdmin
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from .models import Resident, Employee, CommunityEvent

# class EmployeeAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal Info', {'fields': ('employee_name', 'employee_contact_number', 'employee_email_id')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'assigned_groups')}),
#     )
#     filter_horizontal = ('user_permissions', 'assigned_groups')

#     list_display = ('username', 'employee_email_id', 'employee_name', 'is_active', 'is_staff')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'assigned_groups')
#     ordering = ('username',)

# class GroupPermissionInline(admin.TabularInline):
#     model = Permission
#     fields = ('name', 'codename')
#     readonly_fields = ('name', 'codename')
#     can_delete = False
#     max_num = 0
#     show_change_link = True

# class CustomGroupAdmin(GroupAdmin):
#     inlines = [GroupPermissionInline]

# admin.site.register(Resident)
# admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(CommunityEvent)
# admin.site.unregister(Group)
# admin.site.register(Group, CustomGroupAdmin)
# admin.site.unregister(ContentType)
# admin.site.register(ContentType)

