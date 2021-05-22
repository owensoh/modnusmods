from urllib.request import urlopen
import json

def get_classes(acad_year, module_code, sem):

	## url to get module information of given module in given year
	url = "https://api.nusmods.com/v2/" + acad_year + "/modules/" + module_code + ".json"

	response = urlopen(url)
	data_json = json.loads(response.read())

	## semesterData has the data for the timetable schedule for given sem
	semesterData = data_json["semesterData"][sem - 1]["timetable"]
	print(semesterData)
