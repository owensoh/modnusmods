import nusmod_api_getter as func
import classes

if __name__ == "__main__":
	
	module = func.create_module_class("2020-2021", "CS1231S", 1)
	param = classes.Parameters([8, 9, 10, 11, 2, 3, 4, 5], [9, 10, 11, 12, 3, 4, 5, 6], 1, "Online", "Friday")
	parsed_module = func.parameterise(module, "CS1231S", param)

	timetable = classes.Timetable()
	print(timetable)