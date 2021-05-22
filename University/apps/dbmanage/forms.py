from django import forms
from .models import *

class SubjectInputForm(forms.Form):
    subject_name = forms.CharField(max_length = 50, label = 'Название предмета', widget = forms.TextInput(attrs={'class' : "form-control form-control-sm"}))
    subject_price = forms.IntegerField(required=True, label = 'Цена предмета', widget = forms.TextInput(attrs={'onkeydown' : "refresh();", 'class' : "form-control form-control-sm"}))
    subject_l_count = forms.IntegerField(label = 'Кол-во лекций' , initial = Subject._meta.get_field('subject_l_count').get_default() , widget = forms.TextInput(attrs={'onkeydown' : "refresh();", 'class' : "form-control form-control-sm"}))
    subject_p_count = forms.IntegerField(label = 'Кол-во практик', initial = Subject._meta.get_field('subject_p_count').get_default(), widget = forms.TextInput(attrs={'onkeydown' : "refresh();", 'class' : "form-control form-control-sm"}))
    subject_l_price = forms.FloatField(label = 'Цена лекции' , initial = Subject._meta.get_field('subject_l_price').get_default(), widget = forms.TextInput(attrs={'onkeydown' : "refresh();", 'class' : "form-control form-control-sm"}))
    subject_p_price = forms.FloatField(label = 'Цена практики' , initial = Subject._meta.get_field('subject_p_price').get_default(), widget = forms.TextInput(attrs={'onkeydown' : "refresh();", 'class' : "form-control form-control-sm"}))
    whole_price = forms.FloatField(label = 'Общая цена за предмет' , widget=forms.TextInput(attrs={'readonly': 'true' , 'class' : "form-control form-control-sm"}))

class TeacherInputForm(forms.Form):
	teacher_name = forms.CharField(max_length = 50, label = 'ФИО',widget = forms.TextInput(attrs={'class' : "form-control form-control-sm"}))
	teacher_phone = forms.CharField(max_length = 16, label = 'Телефон' , widget = forms.TextInput(attrs={'class' : "form-control form-control-sm"}))
	teacher_exp = forms.IntegerField(label = 'Стаж' , widget = forms.TextInput(attrs={'class' : "form-control form-control-sm"}))

class StudentInputForm(forms.Form):
	student_name = forms.CharField(max_length = 255, label = 'ФИО' , widget = forms.TextInput(attrs={'class' : "form-control form-control-sm"}))
	group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None,  label = 'Группа' , widget = forms.Select(attrs={'class' : "form-select form-select-m"}))

class GroupInputForm(forms.Form):
	DEPARTS = (
		('FT' , 'Дневное'),
		('PT' , 'Заочное'),
	)
	group_name = forms.CharField(max_length = 20, label = 'Название'  , widget = forms.TextInput(attrs={'class' : "form-control form-control-m"}))
	group_depart = forms.ChoiceField(choices = DEPARTS, label = "Отделение" , widget = forms.Select(attrs={'class' : "form-control form-control-m"}))

class ClassesInputForm(forms.Form):
	group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None,  label = 'Группа'  , widget = forms.Select(attrs={'class' : "form-control form-control-m"}))
	teacher = forms.ModelChoiceField(queryset=Teacher.objects.all() , empty_label=None,  label = 'Преподаватель' , widget = forms.Select(attrs={'class' : "form-control form-control-m"}))
	subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label=None,  label = 'Предмет'  , widget = forms.Select(attrs={'class' : "form-control form-control-m"}))

class TeacherForm(forms.Form):
	teacher = forms.ModelChoiceField(queryset=Teacher.objects.all() , empty_label=None,  label = 'Преподаватель' , widget = forms.Select(attrs={'class' : "form-control form-control-m"}))
