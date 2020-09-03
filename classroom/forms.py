from django import forms
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
        fields = ('sap_id', 'graduation_year')

