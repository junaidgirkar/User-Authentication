from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def teacher_home(request):
    return render(request, 'teacher/index.html')


def student_home(request):
    return render(request, 'student/index.html')


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher/register2.html', {'form': form})


"""
def teacher_register(request):
    registered = False
    is_teacher = False
    if request.method == 'POST':
        teacher_form = TeacherSignUpForm(data=request.POST)

        #If forms are valid
        if teacher_form.is_valid():
            teacher = teacher_form.save()
            #Hashing the password
            teacher.set_password(password) # = password
            #teacher.set_password(teacher.password)
            teacher.save()

            is_teacher = True
            registered = True

        else:
            print(teacher_form.errors)

    else:
        teacher_form = TeacherSignUpForm()
    return render(request, 'teacher/register.html', {'teacher_form':teacher_form, 'registered':registered, 'is_teacher': is_teacher})
"""


def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
        return render(request=request,
                      template_name="teacher/login.html",
                      context={"form": form})
    if request.method == 'GET':
        return render(request, 'teacher/login.html')


"""def teacher_login(request):
    if request.method == 'POST':
        # get data from the user filled form
        username = request.POST.get('username')
        password = request.POST.get('password')


        #Checking validity of credentials

        teacher = authenticate(username=username, password=password)
        if teacher:

            if teacher.is_active:
                login(request, teacher)
                return HttpResponseRedirect('/teacher/')
            else:
                return HttpResponse('Your Account is Disabled')
        else:
            print('Invalid Details Provided : {0} {1}'.format(username,password))
            return HttpResponse('Invalid Login Details Provided.')

    else:
        return render(request, 'teacher/login.html', {})"""


@login_required
def teacher_logout(request):
    # Since we are sure the user is logged in
    logout(request)

    # take user back to home page
    return HttpResponseRedirect('/teacher/')


def student_register(request):
    registered = False

    if request.method == 'POST':
        student_form = StudentSignUpForm(data=request.POST, )
        # If form is valid
        if student_form.is_valid():
            student = student_form.save()
            # student.set_password(student.password)
            student.save()
            registered = True
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
        sap_id = request.POST.get('sap_id')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Authentiication of credentials
        student = authenticate(username='username',
                               password='password', email='email')
        if student:
            if student.is_active:
                login(request, student)
                return HttpResponseRedirect('/student/')
            else:
                return HttpResponse('Your Account is disabled')
        else:
            print('Invalid Details Provided: {0} {1}'.format(
                username, password))
            return HttpResponse('Invalid Login Details Provided')
    else:
        return render(request, 'student/login.html', {})


@login_required
def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/student/')
