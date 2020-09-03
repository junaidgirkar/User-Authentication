from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import (Teacher, Student, User)

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_admin','is_student', 'is_teacher', 'first_name', 'last_name')
    filter_horizontal = ()
    search_fields = ("email", 'sap_id', 'is_admin',)
    readonly_fields = (
        'date_joined',
        'last_login',
    )
    list_filter = ()
    fieldsets = ()
    ordering = ['email',]

class StudentAdmin(UserAdmin):
    list_display = ('email','first_name','last_name', 'sap_id','department','dob', 'graduation_year')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email',]

class TeacherAdmin(UserAdmin):
    list_display = ('email','first_name', 'last_name','sap_id', 'dob', 'qualification')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ['email',]
# Register your models here.
admin.site.unregister(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User, CustomUserAdmin)
