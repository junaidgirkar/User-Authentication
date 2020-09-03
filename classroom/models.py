from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager, StudentManager, TeacherManager

class User(AbstractBaseUser, PermissionsMixin):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    email = models.EmailField(_('email address'), blank=True, max_length = 50, unique=True)
    username = models.CharField(_('username'), max_length=255, unique=True, default='default')
    password = models.CharField(_('password'), max_length=255)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    #date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True, null=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_admin = models.BooleanField(_('admin'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    picture = models.ImageField(upload_to='picture/', null=True, blank=True)
    sap_id = models.CharField(_('sap_id'), max_length=11, blank=True, )
    dob = models.DateField(_('dob'), blank=True, null=True)
    department = models.CharField(_('department'), max_length=255, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def is_teacher_check(self):
        return self.is_teacher

    def is_student_check(self):
        return self.is_student

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Student(User, AbstractBaseUser):
    #student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False)
    graduation_year = models.CharField(_('graduation year'), max_length=4, blank=True)
    is_student = True
    #email = models.EmailField(_('email address'), blank=True, max_length=50)
    #sap_id = models.CharField(_('sap_id'), max_length =11, blank=True)
    #username = models.CharField(_('username'), max_length=255, unique=True, default='default')
    #first_name = models.CharField(_('first name'), max_length=30, blank=True)
    #last_name = models.CharField(_('last name'), max_length=30, blank=True)
    #password = models.CharField(_('password'), max_length=255)

    objects = StudentManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Teacher(User, AbstractBaseUser):
    #teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(_('qualification'), max_length =255, blank=True, null=True)
    is_teacher = True
    #email = models.EmailField(_('email address'), blank=True, max_length=50)
    #username = models.CharField(_('username'), max_length=255, unique=True, default='default')
    #password = models.CharField(_('password'), max_length=255)
    #first_name = models.CharField(_('first name'), max_length=30, blank=True)
    #last_name = models.CharField(_('last name'), max_length=30, blank=True)
    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
