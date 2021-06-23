from urllib.request import urlopen
import json
import classes
import operator

def create_module_class(acad_year, module_code, sem):

	## url to get module information of given module in given year
	url = "https://api.nusmods.com/v2/" + acad_year + "/modules/" + module_code + ".json"

	response = urlopen(url)
	data_json = json.loads(response.read())

	## semesterData has the data for the timetable schedule for given sem
	semesterData = data_json["semesterData"][sem - 1]["timetable"]
	
	module = classes.Module(module_code)

	for lesson in semesterData:
		new_lesson = classes.Lesson(lesson['classNo'], int(lesson['startTime'][:2]), int(lesson['endTime'][:2]), lesson['weeks'], lesson['venue'], 
					  lesson['day'], lesson['lessonType'], lesson['size'], lesson['covidZone'], module_code)
		if (lesson['lessonType'].startswith('Tutorial')):
			module.addTutorial(new_lesson)
		elif (lesson['lessonType'] == 'Lecture'):
			module.addLecture(new_lesson)
			#if module_code == 'ST2334':
			#	print(new_lesson.classNo, new_lesson.startTime, new_lesson.endTime)
		elif (lesson['lessonType'].startswith('Laboratory')):
			module.addLaboratory(new_lesson)
	
	return module

def parameterise(module, module_code, parameters):
	new_module = classes.Module(module_code)
	nullLesson = classes.Lesson("", 0, 0, [], "", "", "None", "", "", "")

	## Filter by time of lesson and day off first

	print(module_code, module.lecture_list[0].classNo)
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

	return new_module

## IMPT @NOMP.RONG USE THIS
## args takes in all modules the student input
def create_student(acad_year, sem, *args):
	
	moduleList = []
	nullLesson = classes.Lesson("", 0, 0, [], "", "", "None", "", "", "")
	module_dict = {}

	for module_code in args:
		mod = create_module_class(acad_year, module_code, sem)
		mod.updateLength()
		module_dict[module_code] = [[], [], []]
		if mod.lecture_list != [nullLesson] or mod.laboratory_list != [nullLesson] \
			or mod.tutorial_list != [nullLesson]: ##Ignore mods like MA1521 without lessons
			moduleList.append(mod)
	student = classes.Student(moduleList, module_dict)
	student.forceLecture()
	
	return student

