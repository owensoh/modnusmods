from urllib.request import urlopen
import json
import classes

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
		if (lesson['lessonType'] == 'Tutorial'):
			module.addTutorial(new_lesson)
		elif (lesson['lessonType'] == 'Lecture'):
			module.addLecture(new_lesson)
	
	return module

def parameterise(module, module_code, parameters):
	new_module = classes.Module(module_code)

	## Filter by time of lesson and day off first
	for lesson in module.lecture_list:
		if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):
			new_module.addLecture(lesson)
			

	for lesson in module.tutorial_list:
		if (lesson.day != parameters.dayFree and lesson.startTime in parameters.startTimeList and lesson.endTime in parameters.endTimeList):

			## add if online/both option selected
			if (parameters.lessonMode != 'f2f' and lesson.venue == 'E-Learn_C'):
				new_module.addTutorial(lesson)

			## add if f2f/both option selected
			if (parameters.lessonMode != 'online' and lesson.venue != 'E-Learn_C'):
				new_module.addTutorial(lesson)
