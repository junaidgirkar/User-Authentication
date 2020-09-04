from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('teacher/', views.teacher_home, name="teacher_home"),
    path('teacher/register/', views.teacher_register, name="teacher_register"),
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('teacher/logout/', views.teacher_logout, name='teacher_logout'),

    path('student/', views.student_home, name='student_home'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/logout/', views.student_logout,{'next_page': '/'}, name='student_logoout'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),

]