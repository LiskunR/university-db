from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from .stparse import *
from .filters import *
import random

def index(request):
    if request.method == 'POST':
            form = TeacherForm(request.POST)
            if form.is_valid():
                groups = []
                for cl in Classes.objects.filter(teacher__teacher_name__contains = form.cleaned_data['teacher'].teacher_name):
                    if not any(a['group'] == cl.group.group_name for a in groups):
                        groups.append({'group': cl.group.group_name, 'teacher': cl.teacher.teacher_name, 'price': float(cl.subject.whole_price), 'total':int(cl.subject.total_hours), 'subjects': cl.subject.subject_name})
                    else:
                        for gr in groups:
                            if gr['group'] in cl.group.group_name:
                                gr['total'] += int(cl.subject.total_hours)
                                gr['price'] += float(cl.subject.whole_price)
                                gr['subjects'] += ", " + cl.subject.subject_name
                    print(groups)
                context = {
                    'teachers':Teacher.objects.all(),
                    'students':Student.objects.all(),
                    'groups':Group.objects.all(),
                    'subjects':Subject.objects.all(),
                    'teachersbj':Classes.objects.all(),
                    'teacherclasses': groups,
                    'form': form,
                }
                return render(request, 'dbmanage/index.html', context)
            else:
                form = TeacherForm()
                context = {
                    'teachers':Teacher.objects.all(),
                    'students':Student.objects.all(),
                    'groups':Group.objects.all(),
                    'subjects':Subject.objects.all(),
                    'teachersbj':Classes.objects.all(),
                    'form': form,
                }
                return render(request, 'dbmanage/index.html', context)
    else:
        form = TeacherForm()
        context = {
            'teachers':Teacher.objects.all(),
            'students':Student.objects.all(),
            'groups':Group.objects.all(),
            'subjects':Subject.objects.all(),
            'teachersbj':Classes.objects.all(),
            'form': form,
        }
        return render(request, 'dbmanage/index.html' , context)

######################################################

##################################################################


def teacher_manager(request):
        teachers = Teacher.objects.all()
        if request.method == 'POST':
            form = TeacherInputForm(request.POST)
            if form.is_valid():
                obj, created = Teacher.objects.update_or_create(
                    teacher_name=form.cleaned_data['teacher_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('teacher_manager')
            else:
                form = TeacherInputForm()
                context = {
                'teachers':teachers,
                'form':form,
                }
            return render(request, 'dbmanage/teacher_form.html', context)
        elif 'text' in request.GET and request.GET['text']:
            teachers = Teacher.objects.filter(Q(teacher_name__contains = request.GET['text']) | Q(id__icontains = request.GET['text']) | Q(teacher_phone__icontains = request.GET['text'])).all()
            if request.method == 'POST':
                form = TeacherInputForm(request.POST)
                if form.is_valid():
                    obj, created = Teacher.objects.update_or_create(
                        teacher_name=form.cleaned_data['teacher_name'],
                        defaults = {**form.cleaned_data},
                    )
                    obj.save()
                    return redirect('teacher_manager')
            else:
                form = TeacherInputForm()
                context = {
                'teachers':teachers,
                'form':form,
                }
            return render(request, 'dbmanage/teacher_form.html', context)
        elif 'filter_by' in request.GET and request.GET['filter_by']:
            teachers = teacher_filter(request.GET['filter_from'] ,  request.GET['filter_to'] , request.GET['filter_by'])
            if request.method == 'POST':
                form = TeacherInputForm(request.POST)
                if form.is_valid():
                    obj, created = Teacher.objects.update_or_create(
                        teacher_name=form.cleaned_data['teacher_name'],
                        defaults = {**form.cleaned_data},
                    )
                    obj.save()
                    return redirect('teacher_manager')
            else:
                form = TeacherInputForm()
                context = {
                'teachers':teachers,
                'form':form,
                }
            return render(request, 'dbmanage/teacher_form.html', context)
        else:
            form = TeacherInputForm()
            context = {
            'teachers':teachers,
            'form':form,
            }
            return render(request, 'dbmanage/teacher_form.html', context)

##################################################################

def student_manager(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentInputForm(request.POST)
        if form.is_valid():
            obj, created = Student.objects.update_or_create(
                student_name=form.cleaned_data['student_name'],
                defaults = {**form.cleaned_data},
            )
            obj.save()
            return redirect('student_manager')
    elif 'text' in request.GET and request.GET['text']:
        students = Student.objects.filter(Q(student_name__contains = request.GET['text']) | Q(id__icontains = request.GET['text']) | Q(group__group_name__contains = request.GET['text'])).all()
        if request.method == 'POST':
            form = StudentInputForm(request.POST)
            if form.is_valid():
                obj, created = Student.objects.update_or_create(
                    student_name=form.cleaned_data['student_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('students')
        else:
            form = StudentInputForm()
            context = {
            'students':students,
            'form':form,
            }
        return render(request, 'dbmanage/student_form.html', context)
    elif 'filter_by' in request.GET and request.GET['filter_by']:
        students = student_filter(request.GET['filter_from'] ,  request.GET['filter_to'] , request.GET['filter_by'])
        if request.method == 'POST':
            form = StudentInputForm(request.POST)
            if form.is_valid():
                obj, created = Student.objects.update_or_create(
                    student_name=form.cleaned_data['student_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('students')
        else:
            form = StudentInputForm()
            context = {
            'students':students,
            'form':form,
            }
        return render(request, 'dbmanage/student_form.html', context)
    else:
        form = StudentInputForm()
        context = {
        'students':students,
        'form':form,
        }
        return render(request, 'dbmanage/student_form.html', context)

##################################################################


def subject_manager(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        form = SubjectInputForm(request.POST)
        if form.is_valid():
            obj, created = Subject.objects.update_or_create(
                subject_name=form.cleaned_data['subject_name'],
                defaults = {**form.cleaned_data},
            )
            obj.save()
            return redirect('subject_manager')
        else:
            form = SubjectInputForm()
            context = {
            'subjects':subjects,
            'form':form,
            }
        return render(request, 'dbmanage/subject_form.html', context)
    elif 'text' in request.GET and request.GET['text']:
        subjects = Subject.objects.filter(Q(subject_name__contains = request.GET['text']) | Q(id__icontains = request.GET['text'])).all()
        if request.method == 'POST':
            form = StudentInputForm(request.POST)
            if form.is_valid():
                obj, created = Subject.objects.update_or_create(
                    subject_name=form.cleaned_data['subject_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('subject_manager')
        else:
            form = SubjectInputForm()
            context = {
            'subjects':subjects,
            'form':form,
            }
        return render(request, 'dbmanage/subject_form.html', context)
    elif 'filter_by' in request.GET and request.GET['filter_by']:
        subjects = subject_filter(request.GET['filter_from'] ,  request.GET['filter_to'] , request.GET['filter_by'])
        if request.method == 'POST':
            form = SubjectInputForm(request.POST)
            if form.is_valid():
                obj, created = Subject.objects.update_or_create(
                    subject_name=form.cleaned_data['subject_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('subject_manager')
        else:
            form = SubjectInputForm()
            context = {
            'subjects':subjects,
            'form':form,
            }
        return render(request, 'dbmanage/subject_form.html', context)
    else:
        form = SubjectInputForm()
        context = {
        'subjects':subjects,
        'form':form,
        }
        return render(request, 'dbmanage/subject_form.html', context)


##################################################################

def teachersbj_manager(request):
    teachersbj = Classes.objects.all()
    if request.method == 'POST':
        form = ClassesInputForm(request.POST)
        if form.is_valid():
            obj, created = Classes.objects.update_or_create(
                teacher=form.cleaned_data['teacher'],
                group=form.cleaned_data['group'],
                subject=form.cleaned_data['subject'],
                defaults = {**form.cleaned_data},
            )
            obj.save()
            return redirect('teachersbj_manager')
        else:
            form = ClassesInputForm()
            context = {
            'teacherssbj':teacherssbj,
            'form':form,
            }
        return render(request, 'dbmanage/teachersbj_form.html', context)
    elif 'text' in request.GET and request.GET['text']:
        teachersbj = Classes.objects.filter(Q(teacher__teacher_name__contains = request.GET['text'])| Q(subject__subject_name__contains = request.GET['text']) | Q(group__group_name__contains = request.GET['text']) ).all()
        if request.method == 'POST':
            form = ClassesInputForm()
            if form.is_valid():
                obj, created = Classes.objects.update_or_create(
                    teacher=form.cleaned_data['teacher'],
                    group=form.cleaned_data['group'],
                    subject=form.cleaned_data['subject'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('teachersbj_manager')
        else:
            form = ClassesInputForm()
            context = {
            'teachersbj':teachersbj,
            'form':form,
            }
        return render(request, 'dbmanage/teachersbj_form.html', context)
    elif 'filter_by' in request.GET and request.GET['filter_by']:
        teachersbj = teachersbj_filter(request.GET['filter_from'] ,  request.GET['filter_to'] , request.GET['filter_by'])
        if request.method == 'POST':
            form = ClassesInputForm(request.POST)
            if form.is_valid():
                obj, created = Classes.objects.update_or_create(
                    teacher=form.cleaned_data['teacher'],
                    group=form.cleaned_data['group'],
                    subject=form.cleaned_data['subject'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('teachersbj_manager')
        else:
            form = ClassesInputForm()
            context = {
            'teachersbj':teachersbj,
            'form':form,
            }
        return render(request, 'dbmanage/teachersbj_form.html', context)
    else:
        form = ClassesInputForm()
        context = {
        'teachersbj':teachersbj,
        'form':form,
        }
        return render(request, 'dbmanage/teachersbj_form.html', context)

##################################################################

def group_manager(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        form = GroupInputForm(request.POST)
        if form.is_valid():
            obj, created = Group.objects.update_or_create(
                group_name=form.cleaned_data['group_name'],
                defaults = {**form.cleaned_data},
            )
            obj.save()
            return redirect('group_manager')
        else:
            form = GroupInputForm()
            context = {
            'groups':groups,
            'form':form,
            }
        return render(request, 'dbmanage/group_form.html', context)
    elif 'text' in request.GET and request.GET['text']:
        groups = Group.objects.filter(Q(group_name__contains = request.GET['text']) | Q(group_depart__contains = request.GET['text']) | Q(id__icontains = request.GET['text'])).all()
        if request.method == 'POST':
            form = GroupInputForm(request.POST)
            if form.is_valid():
                obj, created = Group.objects.update_or_create(
                    group_name=form.cleaned_data['group_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('group_manager')
        else:
            form = GroupInputForm()
            context = {
            'groups':groups,
            'form':form,
            }
        return render(request, 'dbmanage/group_form.html', context)
    elif 'filter_by' in request.GET and request.GET['filter_by']:
        groups = group_filter(request.GET['filter_from'] ,  request.GET['filter_to'] , request.GET['filter_by'])
        if request.method == 'POST':
            form = GroupInputForm(request.POST)
            if form.is_valid():
                obj, created = Group.objects.update_or_create(
                    subject_name=form.cleaned_data['subject_name'],
                    defaults = {**form.cleaned_data},
                )
                obj.save()
                return redirect('group_manager')
        else:
            form = GroupInputForm()
            context = {
            'groups':groups,
            'form':form,
            }
        return render(request, 'dbmanage/group_form.html', context)
    else:
        form = GroupInputForm()
        context = {
        'groups':groups,
        'form':form,
        }
        return render(request, 'dbmanage/group_form.html', context)
