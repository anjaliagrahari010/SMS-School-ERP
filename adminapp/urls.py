from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('dash',views.index,name="dash"),
    path('teacher',views.teacher,name="teacher"),
    path('student',views.student,name="student"),
    path('attendance',views.attendance,name="attendance"),
    path('classes',views.classes,name="classes"),
    path('subjects',views.subjects,name="subjects"),
    path('logout',views.logout,name="logout"),
    path('delteacher/<id>',views.delteacher,name="delteacher"),
    path('edit/<id>',views.edit,name="edit"),
    path('delstudent/<id>', views.delstudent, name = "delstudent"),
    path('edit_teacher/<id>', views.edit_teacher, name = "edit_teacher"),
    path('edit-class/<id>',views.editclass,name="editclass"),
    path('delsubject/<id>', views.delsubject, name="delsubject"),
    path('viewenquiries/',views.viewenquiries,name="viewenquiries"),
    path('admincp/',views.admincp,name="admincp"),
    path('delclass/<id>', views.delclass, name="delclass"),
]



