from django.urls import path
from . import views
from .stparse import *

urlpatterns = [
    path('' , views.index, name = 'index'),
    path('teachers', views.teacher_manager, name='teacher_manager'),
    path('teachers/parse', teachers_create, name='teachers_create'),
    path('students/parse', students_create, name='students_create'),
    path('subjects', views.subject_manager, name='subject_manager'),
    path('subjects/parse', subject_create, name='subject_create'),
    path('students', views.student_manager, name='student_manager'),
    path('groups', views.group_manager, name='group_manager'),
    path('teachersubjects', views.teachersbj_manager, name='teachersbj_manager'),
    path('delete/<name>/<int:id>/', delete_object),
    path('delete/<name>/all', delete_all),
]
