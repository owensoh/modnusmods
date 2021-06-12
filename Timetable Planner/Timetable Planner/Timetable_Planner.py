import nusmod_api_getter as func
import classes

if __name__ == "__main__":
	
	param = classes.Parameters([10, 11, 14, 15, 16, 17], [11, 12, 15, 16, 17, 18], 1, "online", "Friday")

	#param = classes.Parameters([10, 11, 14, 15], [11, 12, 15, 16], 1, "Online", "Friday")

	#param = classes.Parameters([10, 11, 14, 15, 16, 17], [11, 12, 15, 16, 17, 18], 2, "online", "Friday")

	student = func.create_student("2020-2021", 2, "CS2100", "CS2040C", "MA1521", "CS1231S", "MA1101R")
	# https://nusmods.com/timetable/sem-2/share?CS1231S=LEC:1,TUT:03&CS2040C=LAB:10,LEC:1&CS2100=TUT:01,LAB:13,LEC:1&MA1101R=TUT:3,LEC:2&MA1521=



	#When got repeated lecture slots it prints error 
	#student = func.create_student("2020-2021", 2, "CS2100", "CS2040C", "JS1101E", "CS1231S", "MA1101R")
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
			link = student.generateNusmodsLink()
			print(link)

#Test Cases:

#1) All works and a timetable is shown
#2) Lecture clashes right from the start, timetable cannot be shown
#3) After showing user, lecture/tutorial/laboratory cannot meet parameters, timetable cannot be shown

