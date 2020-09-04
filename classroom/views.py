from django.contrib.auth.models import User, AbstractUser, auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Teacher, Student
from django.views import View
# Create your views here.



def teacher_home(request):
    return render(request, 'teacher/index.html')


def student_home(request):
    return render(request, 'student/index.html')


def teacher_register(request):
    registered = False
    is_teacher = False
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            is_teacher = True
            registered = True
            #username = User.objects.get(email=form.cleaned_data['email'])

            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return render(request, 'registration/login.html', {'registered':registered, 'is_teacher':is_teacher})
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher/register2.html', {'form': form, 'registered':registered, 'is_teacher':is_teacher})




def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'teacher/profile.html')
                    #return render(request=request,template_name="teacher/profile.html",context={"form": form})
            else:
                error = 'Invalid Username or Password'
    if request.method == 'GET':
        return render(request, 'teacher/login.html')


@login_required
def teacher_logout(request):
    # Since we are sure the user is logged in
    logout(request)

    # take user back to home page
    return render(request,'teacher/profile.html')


def student_register(request):
    registered = False

    if request.method == 'POST':
        student_form = StudentSignUpForm(data=request.POST, )
        # If form is valid
        if student_form.is_valid():
            student = student_form.save()
            # student.set_password(student.password)
            student.save()
            is_student = True
            registered = True
            return render(request, 'student/index.html', {'registered':registered, 'is_student':is_student})
        else:
            print(student_form.errors)
    else:
        student_form = StudentSignUpForm()
    return render(request, 'student/register2.html', {'student_form': student_form, 'registered': registered})


def student_login(request):
    if request.method == 'POST':

        # Getting Data from Student Filled form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #email = request.POST.get('email')

        # Authentiication of credentials
        student = authenticate(request, username='username',
                               password='password')

        if student is not None:
        #if student.is_active:
            login(request, student, backend='django.contrib.auth.backends.ModelBackend')

            return HttpResponseRedirect('/student/')
        #else:
         #       return HttpResponse('Your Account is disabled')
        else:
            print('Invalid Details Provided: {0} {1}'.format(
                username, password))
            return HttpResponse('Invalid Login Details Provided')
    else:
        return render(request, 'student/login.html', {})


@login_required
def student_logout(request):
    logout(request)
    #return HttpResponseRedirect('/student/')
