from bs4 import BeautifulSoup
import requests
import random
from .views import *

class DataParse(object):

	def get_students(self):
		stlist = {}
		grlist = []
		html = requests.get("https://dsum.edu.ua/uk/angliyska-mova")
		soup = BeautifulSoup(html.text, 'lxml')
		for i in range(0 , 29):
			thead = soup.find_all('table')[i].tbody.find_all("tr")
			for t in thead:
				student = t.find_all('p')[1].text
				group = t.find_all('p')[2].text
				stlist.update({student: group})
				grlist.append(group.upper())
		return stlist , (list(set(grlist)))

	def get_teachers(self):
		tlist = []
		urls = [
		"https://dsum.edu.ua/uk/departments/it",
		"https://dsum.edu.ua/uk/departments/marketing",
		"https://dsum.edu.ua/uk/departments/tourism",
		"https://dsum.edu.ua/uk/departments/fin",
		"https://dsum.edu.ua/uk/departments/ypep",
		"https://dsum.edu.ua/uk/departments/imov",
		"https://dsum.edu.ua/uk/departments/dep-eco-management",
		"https://dsum.edu.ua/uk/departments/puta",
		"https://dsum.edu.ua/uk/departments/dpd"
		]
		for url in urls:
			html = requests.get(url)
			soup = BeautifulSoup(html.text, 'lxml')
			teachers = soup.find("div" , class_="teachers-list").find_all("div", class_="teacher")
			for t in teachers:
				tlist.append(t.find(class_="teacher__name").text)
		return (list(set(tlist)))

	def get_subjects(self):
		sblist = []
		urls = [
		"https://dsum.edu.ua/uk/departments/it",
		"https://dsum.edu.ua/uk/departments/marketing",
		"https://dsum.edu.ua/uk/departments/tourism",
		"https://dsum.edu.ua/uk/departments/fin",
		"https://dsum.edu.ua/uk/departments/ypep",
		"https://dsum.edu.ua/uk/departments/imov",
		]
		for url in urls:
			html = requests.get(url)
			soup = BeautifulSoup(html.text, 'lxml')
			subjects = soup.find("div" , class_="links-list").find_all("a")
			for sb in subjects:
				sblist.append(sb.text.strip())
		return sblist


def students_create(request):
	students , groupslist = DataParse().get_students()
	for gr in groupslist:
		if Group.objects.filter(group_name = gr):
			create_students(students, gr)
		else:
			Group.objects.create(group_name = gr)
			create_students(students, gr)
			return redirect('student_manager')

def create_students(students,gr):
    group = Group.objects.get(group_name = gr)
    for st in students:
        if students[st] == gr:
            obj , created = Student.objects.update_or_create(
                student_name = st,
                group = group,
                defaults = {'student_name': st,'group': group},
            )
            obj.save()

def subjects_create(request):
    subjects = DataParse().get_subjects()
    for s in subjects:
        if not Subject.objects.filter(Q(subject_name = t)):
            subject = Subject.objects.create(
                subject_name = s,
                subject_price = random.randint(10, 100),
                subject_l_count = random.randint(15, 40),
                subject_p_count = random.randint(20, 40),
                subject_l_price = random.randint(25, 50),
                subject_p_price = random.randint(30, 60),
            )
            subject.save()
    return redirect('subject_manager')


def teachers_create(request):
    teachers = DataParse().get_teachers()
    for t in teachers:
        phone = '+3809'+str(random.randint(11111111, 99999999))
        if not Teacher.objects.filter(Q(teacher_name = t) | Q(teacher_phone = phone)):
            teacher = Teacher.objects.create(
                teacher_name = t,
                teacher_exp = random.randint(100, 1000),
                teacher_phone = phone,
            )
            teacher.save()
    return redirect('teacher_manager')

def subject_create(request):
    subjects = DataParse().get_subjects()
    for sb in subjects:
        if not Subject.objects.filter(subject_name = sb):
            subject = Subject.objects.create(
                subject_name = sb,
                subject_price = random.randint(10, 20),
                subject_l_count = random.randint(20, 40),
                subject_p_count = random.randint(15, 40),
            )
            subject.save()
    return redirect('subject_manager')


def delete_object(request, id , name):
    if name == "teachers":
        Teacher.objects.filter(id=id).delete()
        return redirect('teacher_manager')
    elif name == "groups":
        Group.objects.filter(id=id).delete()
        return redirect('group_manager')
    elif name == "subjects":
        Subject.objects.filter(id=id).delete()
        return redirect('subject_manager')
    elif name == "students":
        Student.objects.filter(id=id).delete()
        return redirect('student_manager')
    elif name == "teachersbj":
        Classes.objects.filter(id=id).delete()
        return redirect('teachersbj_manager')
    else:
        return HttpResponse("ERROR")