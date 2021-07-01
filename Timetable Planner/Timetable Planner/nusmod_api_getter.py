from urllib.request import urlopen
import json
import classes
import operator
from copy import deepcopy

def create_module_class(acad_year, module_code, sem):

	## url to get module information of given module in given year
	url = "https://api.nusmods.com/v2/" + acad_year + "/modules/" + module_code + ".json"

	response = urlopen(url)
	data_json = json.loads(response.read())

	## semesterData has the data for the timetable schedule for given sem
	semesterData = data_json["semesterData"][sem - 1]["timetable"]
	
	module = classes.Module(module_code)

	for lesson in semesterData:
		new_lesson = classes.Lesson(lesson['classNo'], int(lesson['startTime'][:2]), \
			int(lesson['endTime'][:2]) + int(lesson['endTime'][-2] != '0'), lesson['weeks'], \
			lesson['venue'], lesson['day'], lesson['lessonType'], lesson['size'], lesson['covidZone'], module_code, lesson['startTime'], lesson['endTime'])
		if (lesson['lessonType'].startswith('Tutorial')):
			module.addTutorial(new_lesson)
		elif (lesson['lessonType'] == 'Lecture'):
			module.addLecture(new_lesson)
		elif (lesson['lessonType'].startswith('Laboratory')):
			module.addLaboratory(new_lesson)
		elif (lesson['lessonType'].startswith('Sectional')):
			module.addSectional(new_lesson)
	
	return module

def parameterise(module, module_code, parameters):
	new_module = classes.Module(module_code)
	nullLesson = classes.Lesson("", 0, 0, [], "", "", "None", "", "", "", "", "")

	## Filter by time of lesson and day off first

	#print(module_code, module.lecture_list[0].classNo)
	if len(module.lecture_list) > 1:
		new_module.resetLecture()

	if module.lecture_list == [nullLesson]:
		new_module.addLecture(nullLesson)
	else:

		for lesson in module.lecture_list:
			if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):
				new_module.addLecture(lesson)
			else:
				for otherLesson in module.lecture_list:
					if otherLesson.classNo == lesson.classNo:
						new_module.removeLecture(otherLesson)

	if len(module.tutorial_list) > 1:
		new_module.resetTutorial()

	for lesson in module.tutorial_list:

		if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):

			if parameters.lessonMode == 'f2f':
				if lesson.venue.startswith('E-Learn'):
					lesson.lessonTypeNumber = 1
				else:
					lesson.lessonTypeNumber = 0
			elif parameters.lessonMode == 'online':
				if lesson.venue.startswith('E-Learn'):
					lesson.lessonTypeNumber = 0
				else:
					lesson.lessonTypeNumber = 1
			
			new_module.addTutorial(lesson)
	new_module.tutorial_list = sorted(new_module.tutorial_list, key=operator.attrgetter('lessonTypeNumber'))

	if len(module.laboratory_list) > 1:
		new_module.resetLaboratory()

	for lesson in module.laboratory_list:
		if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):

			if parameters.lessonMode == 'f2f':
				if lesson.venue.startswith('E-Learn'):
					lesson.lessonTypeNumber = 1
				else:
					lesson.lessonTypeNumber = 0
			elif parameters.lessonMode == 'online':
				if lesson.venue.startswith('E-Learn'):
					lesson.lessonTypeNumber = 0
				else:
					lesson.lessonTypeNumber = 1
			
			new_module.addLaboratory(lesson)
	new_module.laboratory_list = sorted(new_module.laboratory_list, key=operator.attrgetter('lessonTypeNumber'))

	if len(module.sectional_list) > 1:
		new_module.resetLaboratory()

	#for lesson in module.sectional_list:
	#	if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):

	#		if parameters.lessonMode == 'f2f':
	#			if lesson.venue.startswith('E-Learn'):
	#				lesson.lessonTypeNumber = 1
	#			else:
	#				lesson.lessonTypeNumber = 0
	#		elif parameters.lessonMode == 'online':
	#			if lesson.venue.startswith('E-Learn'):
	#				lesson.lessonTypeNumber = 0
	#			else:
	#				lesson.lessonTypeNumber = 1
			
	#		new_module.addLaboratory(lesson)
	#new_module.sectional_list = sorted(new_module.sectional_list, key=operator.attrgetter('lessonTypeNumber'))

	if len(module.sectional_list) > 1:
		new_module.resetSectional()

	if module.lecture_list == [nullLesson]:
		new_module.addSectional(nullLesson)
	else:

		for lesson in module.sectional_list:
			if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):
				new_module.addSectional(lesson)
			else:
				for otherLesson in module.lecture_list:
					if otherLesson.classNo == lesson.classNo:
						new_module.removeSectional(otherLesson)

	return new_module

def get_common_mods(modules1, modules2):
	comm = []
	for module in modules1:
		if module in modules2:
			comm.append(module)

	return comm

## args takes in all modules the student input
def create_student(acad_year, sem, modules, user):
	
	nullLesson = classes.Lesson("", 0, 0, [], "", "", "None", "", "", "", "", "")
	moduleList = []
	module_dict = []

	for lst in modules:
		moduleListSub = []
		module_dict_sub = {}

		for module_code in lst:
			mod = create_module_class(acad_year, module_code, sem)
			mod.updateLength()
			module_dict_sub[module_code] = [[], [], [], []]
			if mod.lecture_list != [nullLesson] or mod.laboratory_list != [nullLesson] \
				or mod.tutorial_list != [nullLesson] or mod.sectional_list != [nullLesson]: ##Ignore mods like MA1521 without lessons
				moduleListSub.append(mod)
		moduleList.append(moduleListSub)
		module_dict.append(module_dict_sub)

	student = classes.Student(moduleList, module_dict, user, get_common_mods(moduleList[0], moduleList[1]))
	student.forceLecture()
	
	return student


def parseJianrong(dict, user=1):
	startTimeList = []
	endTimeList = []
	acadYear = ""
	sem = 0
	timeBetween = 0
	lessonMode = ""
	dayFree = ""
	modules = []
	for i in range(int(dict['startTime']), int(dict['endTime'])):
		startTimeList.append(i)
		endTimeList.append(i+1)
	if dict['lunchBreak']:
		startTimeList.remove(12)
		startTimeList.remove(13)
		endTimeList.remove(13)
		endTimeList.remove(14)
	lessonMode = dict['lessonMode']
	timeBetween = int(dict['timeBetween'])
	dayFree = dict['dayFree']
	sem = int(dict['sem'])
	acadYear = dict['acadYear']

	if user == 1:
		modules = dict['modules']

		return classes.Parameters(startTimeList, endTimeList, timeBetween, lessonMode, dayFree),\
			sem, create_student(acadYear, sem, [modules, []], user)
	elif user == 2:
		modules1 = dict['modules1']
		modules2 = dict['modules2']

		return classes.Parameters(startTimeList, endTimeList, timeBetween, lessonMode, dayFree),\
			sem, create_student(acadYear, sem, [modules1, modules2], user)

