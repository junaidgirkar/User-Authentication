"""from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Teacher, Student, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('qualification',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('sap_id', 'graduation_year')"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Teacher


class StudentSignUpForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    sap_id = forms.CharField(max_length=11, help_text='SAP ID', required=False)
    dob = forms.DateField(required=True, help_text='Date Of Birth')
    department = forms.CharField(max_length=255, help_text='Department/Branch Name', required=False)
    graduation_year = forms.CharField(max_length=4, required=False)
    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name', 'email','sap_id','dob', 'department','graduation_year', 'password1', 'password2')

class TeacherSignUpForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    sap_id = forms.CharField(max_length=11, help_text='SAP ID', required=False)
    dob = forms.DateField(required=True, help_text='Date Of Birth')
    department = forms.CharField(max_length=255, help_text='Department/Branch Name', required=False)
    qualification = forms.CharField(max_length=255, required=False)
    class Meta:
        model = Teacher
        fields = ('username', 'first_name', 'last_name', 'email','sap_id', 'dob', 'department', 'qualification', 'password1','password2' )

