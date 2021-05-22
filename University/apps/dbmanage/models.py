from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class Group(models.Model):
	DEPARTMENTS = (
		('FT' , 'Дневное'),
		('PT' , 'Заочное'),
	)
	group_name = models.CharField('Группа', max_length = 50)
	group_depart = models.CharField(max_length=2, choices=DEPARTMENTS , default = 'FT')

	class Meta:
	    ordering = ['group_name']

	def __str__(self):
		return self.group_name


class Student(models.Model):
	student_name = models.CharField('ФИО', max_length = 70)
	group = models.ForeignKey(Group, on_delete = models.CASCADE)


	def __str__(self):
		return self.student_name

class Teacher(models.Model):
    teacher_name = models.CharField('ФИО', max_length = 70)
    teacher_phone = models.CharField('Телефон', max_length = 13, unique=True)
    teacher_exp = models.PositiveIntegerField('Стаж')
    teacher_salary = models.FloatField('Зарплата' , editable = False , default = 0)

    def __str__(self):
        return self.teacher_name

class Subject(models.Model):
    subject_name = models.CharField('Название', max_length = 70)
    subject_price = models.PositiveIntegerField('Цена предмета')
    subject_l_count = models.PositiveIntegerField('Кол-во лекций',default = 40)
    subject_p_count = models.PositiveIntegerField('Кол-во практик',default = 0)
    subject_l_price = models.PositiveIntegerField('Цена за лекцию',default = 50)
    subject_p_price = models.PositiveIntegerField('Цена за практику',default = 100)
    whole_price = models.FloatField('Общая цена за предмет', default = 0 , editable = False)
    total_hours = models.PositiveIntegerField('Всего часов',default = 0 , editable = False)

    def save(self,*args,**kwargs):
        self.whole_price = ((self.subject_l_count * self.subject_l_price) + self.subject_price) + ((self.subject_p_count * self.subject_p_price) + self.subject_price)
        self.total_hours = self.subject_p_count + self.subject_l_count
        super(Subject,self).save(*args,**kwargs)

    def __str__(self):
        return self.subject_name

class Classes(models.Model):
	group = models.ForeignKey(Group , on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

	def save(self,*args,**kwargs):
		self.teacher.teacher_salary += self.subject.whole_price
		self.teacher.save()
		super(Classes,self).save(*args,**kwargs)

	def __str__(self):
		return '%s %s %s' % (self.teacher.teacher_name, self.group.group_name, self.subject.subject_name)
