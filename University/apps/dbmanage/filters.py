from .models import *
from django.db.models import Max, Min, Count

def subject_filter(f_from , f_to , f_by):
    subjects = Subject.objects.all()
    if f_from == '':
        f_from = Subject.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_to == '':
        f_to = Subject.objects.all().aggregate(Max(f_by))[f_by+'__max']
    if f_from != '' and f_to != '':
        if f_by == 'id':
            subjects = Subject.objects.filter(id__gte=f_from , id__lte=f_to).all()
        elif f_by == 'subject_price':
            subjects = Subject.objects.filter(subject_price__gte=f_from , subject_price__lte=f_to).all()
        elif f_by == 'subject_l_count':
            subjects = Subject.objects.filter(subject_l_count__gte=f_from , subject_l_count__lte=f_to).all()
        elif f_by == 'subject_p_count':
            subjects = Subject.objects.filter(subject_p_count__gte=f_from , subject_p_count__lte=f_to).all()
        elif f_by == 'subject_l_price':
            subjects = Subject.objects.filter(subject_l_price__gte=f_from , subject_l_price__lte=f_to).all()
        elif f_by == 'subject_p_price':
            subjects = Subject.objects.filter(subject_p_price__gte=f_from , subject_p_price__lte=f_to).all()
        elif f_by == 'whole_price':
            subjects = Subject.objects.filter(whole_price__gte=f_from , whole_price__lte=f_to).all()
    return subjects

def teachersbj_filter(f_from , f_to , f_by):
    teachersbj = TeacherSubject.objects.all()
    if f_from == '':
        if f_by != 'id':
            f_from = TeacherSubject.objects.all().aggregate(Min('subject__' + f_by))['subject__' + f_by+'__min']
        else:
            f_from = TeacherSubject.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_to == '':
        if f_by != 'id':
            f_to = TeacherSubject.objects.all().aggregate(Max('subject__' +f_by))['subject__' +f_by+'__max']
        else:
            f_from = TeacherSubject.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_from != '' and f_to != '':
        if f_by == 'id':
            teachersbj = TeacherSubject.objects.filter(id__gte=f_from , id__lte=f_to).all()
        elif f_by == 'subject_price':
            teachersbj = TeacherSubject.objects.filter(subject__subject_price__gte=f_from , subject__subject_price__lte=f_to).all()
        elif f_by == 'subject_l_count':
            teachersbj = TeacherSubject.objects.filter(subject__subject_l_count__gte=f_from , subject__subject_l_count__lte=f_to).all()
        elif f_by == 'subject_p_count':
            teachersbj = TeacherSubject.objects.filter(subject__subject_p_count__gte=f_from , subject__subject_p_count__lte=f_to).all()
        elif f_by == 'subject_l_price':
            teachersbj = TeacherSubject.objects.filter(subject__subject_l_price__gte=f_from , subject__subject_l_price__lte=f_to).all()
        elif f_by == 'subject_p_price':
            teachersbj = TeacherSubject.objects.filter(subject__subject_p_price__gte=f_from , subject__subject_p_price__lte=f_to).all()
        elif f_by == 'whole_price':
            teachersbj = TeacherSubject.objects.filter(subject__whole_price__gte=f_from , subject__whole_price__lte=f_to).all()
    return teachersbj

def student_filter(f_from , f_to , f_by):
    if f_from == '' and f_to == '':
        return  Student.objects.all()
    if f_from == '':
        f_from = Student.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_to == '':
        f_to = Student.objects.all().aggregate(Max(f_by))[f_by+'__max']
    if f_from != '' and f_to != '':
        if f_by == 'id':
            students = Student.objects.filter(id__gte=f_from , id__lte=f_to).all()
    return students


def teacher_filter(f_from , f_to , f_by):
    if f_from == '' and f_to == '':
        return  Teacher.objects.all()
    if f_from == '':
        f_from = Teacher.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_to == '':
        f_to = Teacher.objects.all().aggregate(Max(f_by))[f_by+'__max']
    if f_from != '' and f_to != '':
        if f_by == 'id':
            teachers = Teacher.objects.filter(id__gte=f_from , id__lte=f_to).all()
        if f_by == 'teacher_exp':
            teachers = Teacher.objects.filter(teacher_exp__gte=f_from , teacher_exp__lte=f_to).all()
        if f_by == 'teacher_lessons_count':
            teachers = Teacher.objects.annotate(cl=Count('classes')).filter(cl__gte=f_from , cl__lte=f_to).all()
        if f_by == 'teacher_salary':
            teachers = Teacher.objects.filter(teacher_salary__gte=f_from , teacher_salary__lte=f_to).all()
    return teachers

def group_filter(f_from , f_to , f_by):
    if f_from == '' and f_to == '':
        return  Group.objects.all()
    if f_from == '':
        f_from = Group.objects.all().aggregate(Min(f_by))[f_by+'__min']
    if f_to == '':
        f_to = Group.objects.all().aggregate(Max(f_by))[f_by+'__max']
    if f_from != '' and f_to != '':
        if f_by == 'id':
            teachers = Group.objects.filter(id__gte=f_from , id__lte=f_to).all()
        if f_by == 'student_set.count':
            teachers = Group.objects.annotate(st=Count('student')).filter(st__gte=f_from , st__lte=f_to).all()
    return teachers

