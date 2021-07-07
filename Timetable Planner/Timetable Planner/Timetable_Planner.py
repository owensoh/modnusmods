import nusmod_api_getter as func
import classes
import webbrowser


def TestCase1():
	# 5 modules, no additional parameters given
	return classes.Parameters([8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 0, "", ""),\
	   1, func.create_student("2021-2022", 1, ["CS2105", "CS2106", "ST2334", "LAJ1201", "CS2113"])

def TestCase2():
	# 5 modules, additional parameters given, but can pass
	return classes.Parameters([8, 9, 10, 11, 14, 15, 16, 17], [9, 10, 11, 12, 15, 16, 17, 18], 1, "online", "Friday"),\
	   1, func.create_student("2021-2022", 1, ["CS2105", "CS2106", "ST2334", "LAJ1201", "CS2113"])

def TestCase3():
	# 5 modules, additional parameters given, fails
	return classes.Parameters([8, 9, 10, 11, 14, 15, 16, 17], [9, 10, 11, 12, 15, 16, 17, 18], 1, "online", "Thursday"),\
	   1, func.create_student("2021-2022", 1, ["CS2105", "CS2106", "ST2334", "LAJ1201", "CS2113"])

def TestCase4():
	# 5 modules, additional parameters given, shows lect, but fails others
	return classes.Parameters([10, 11, 14, 15, 16, 17], [11, 12, 15, 16, 17, 18], 2, "both", "Friday"),\
	   1, func.create_student("2021-2022", 1, ["CS2105", "CS2106", "ST2334", "LAJ1201", "CS2113"])

def TestCase5():
	# 6 modules, no additional parameters given
	return classes.Parameters([8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 0, "online", ""),\
	   1, func.create_student("2021-2022", 1, ["GET1050", "PL3106", "EC2102", "GES1041", "EC2101", "EC3303"])

def TestCase6():
	# 6 modules, additional parameters given, but can pass
	return classes.Parameters([10, 11, 12, 13, 14, 15, 16, 17], [11, 12, 13, 14, 15, 16, 17, 18], 0, "f2f", "Friday"),\
	   1, func.create_student("2021-2022", 1, ["GET1050", "PL3106", "EC2102", "GES1041", "EC2101", "EC3303"])

def TestCase7():
	# 6 modules, additional parameters given, cannot pass
	return classes.Parameters([10, 11, 12, 13, 14, 15, 16, 17], [11, 12, 13, 14, 15, 16, 17, 18], 1, "f2f", ""),\
	   1, func.create_student("2021-2022", 1, ["GET1050", "PL3106", "EC2102", "GES1041", "EC2101", "EC3303"])

def TestCase8():
	# 10 modules, no additional parameters given
	return classes.Parameters([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 0, "", ""),\
	   1, func.create_student("2021-2022", 1, ["BSP2701", "GET1028", "IS1103", "STR2000", "CS2100", "BSP1702", "FIN2704", "CS2040S", "GEH1036", "DAO1704"])

def TestCase9():
	# 10 modules, 1 additional parameters given to fail
	return classes.Parameters([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 1, "", ""),\
	   1, func.create_student("2021-2022", 1, ["BSP2701", "GET1028", "IS1103", "STR2000", "CS2100", "BSP1702", "FIN2704", "CS2040S", "GEH1036", "DAO1704"])

def TestCase10():
	# 10 modules, 1 additional parameters given to pass
	return classes.Parameters([10, 11, 14, 15, 16, 17, 18, 19], [11, 12, 15, 16, 17, 18, 19, 20], 0, "", ""),\
	   1, func.create_student("2021-2022", 1, ["BSP2701", "GET1028", "IS1103", "STR2000", "CS2100", "BSP1702", "FIN2704", "CS2040S", "GEH1036", "DAO1704"])

def newTestCase1():
	return func.parseJianrong({'startTime': '8', 'endTime': '18', 'timeBetween': '1', 'lunchBreak': True, 'lessonMode': 'online',\
	   'dayFree': 'Friday', 'modules': ["CS2105", "CS2106", "ST2334", "LAJ1201", "CS2113"],\
	  'sem': '1', 'acadYear': '2021-2022'})

def newTestCase2():
	return func.parseJianrong({'startTime': '8', 'endTime': '18', 'timeBetween': '0', 'lunchBreak': True, 'lessonMode': 'online',\
	   'dayFree': 'Friday', 'modules': ["CS1010"],\
	  'sem': '1', 'acadYear': '2021-2022'})

def newerTestCase1():
	return func.parseJianrong({'startTime': '8', 'endTime': '18', 'timeBetween': '0', 'lunchBreak': False, 'lessonMode': '',\
	   'dayFree': '', 'modules1': ["CS2105", "CS2106", "ST2334", "CS2113", "LAJ1201", "CS2107"], \
	   'modules2': ["ST2334", "LAJ1201", "CS2107", "CS2100", "GES1041"],
	  'sem': '1', 'acadYear': '2021-2022'}, 2) 

def newerTestCase2():
	return func.parseJianrong({'startTime': '8', 'endTime': '18', 'timeBetween': '1', 'lunchBreak': True, 'lessonMode': '',\
	   'dayFree': '', 'modules1': ["CS2105", "CS2106", "ST2334", "CS2113", "LAJ1201", "CS2107"], \
	   'modules2': ["ST2334", "LAJ1201", "CS2107", "CS2100", "GES1041"],
	  'sem': '1', 'acadYear': '2021-2022'}, 2) 

def newerTestCase3():
	return func.parseJianrong({'startTime': '8', 'endTime': '18', 'timeBetween': '0', 'lunchBreak': False, 'lessonMode': '',\
	   'dayFree': '', 'modules1': ["CS2105", "CS2106", "ST2334", "CS2113", "LAJ1201", "CS2107"], \
	   'modules2': ["CS2030S", "MA1521", "CS2040S", "CS2100", "GES1041"],
	  'sem': '1', 'acadYear': '2021-2022'}, 2) 

def timetable(dict):

    param, sem, student = func.parseJianrong(dict)
    link = ""
    timetable_json = {}


    if student.impossible:
        return False, link, timetable_json
    else:
        print(student)
        print("__")
        student.addParam(param)
        if student.impossible:
            return False, link, timetable_json
        else:
            student.generate(param)
            print(student)
            if student.impossible:
                return False, link, timetable_json
            else:
                link = student.generateNusmodsLink(sem)
                print(link)
                timetable_json = student.timetable_data()
                # FOR TESTING PURPOSES 
                # webbrowser.open(link)
                return True, link, timetable_json

if __name__ == "__main__":
	
	# SEND USER NUMBER HERE
	user = 2

	if user == 1:
		#param, sem, student = TestCase1()
		#param, sem, student = TestCase2()
		#param, sem, student = TestCase3()
		#param, sem, student = TestCase4()
		#param, sem, student = TestCase5()
		#param, sem, student = TestCase6()
		#param, sem, student = TestCase7()
		#param, sem, student = TestCase8()
		#param, sem, student = TestCase9()
		#param, sem, student = TestCase10()
		param, sem, student = newTestCase1()
		#param, sem, student = newTestCase2()

		if student.impossible:
			print("sadge")
		else:
			print(student)
			print("____________")
			student.addParam(param)
			if student.impossible:
				print('sadge')
			else:
				student.generate(param)
				print(student)
				if student.impossible:
					print('sadge')
				else:
					link1 = student.generateNusmodsLink(sem, 1)
					print(link1)

					# FOR TESTING PURPOSES 
					webbrowser.open(link1)

	elif user == 2:

		#param, sem, student = newerTestCase1()
		#param, sem, student = newerTestCase2()
		param, sem, student = newerTestCase3()

		if student.impossible:
			print("sadge")
		else:
			print(student)
			print("____________")
			student.addParam(param)
			if student.impossible:
				print('sadge')
			else:
				student.generate(param)
				print(student)
				if student.impossible:
					print('sadge')
				else:
					link1 = student.generateNusmodsLink(sem, 1)
					print(link1)
					link2 = student.generateNusmodsLink(sem, 2)
					print(link2)

					# FOR TESTING PURPOSES 
					webbrowser.open(link1)
					webbrowser.open(link2)
		


				

#Test Cases:

#1) All works and a timetable is shown

#2) Lecture clashes right from the start, timetable cannot be shown
#3) After showing user, lecture/tutorial/laboratory cannot meet parameters, timetable cannot be shown


#DONEZO
