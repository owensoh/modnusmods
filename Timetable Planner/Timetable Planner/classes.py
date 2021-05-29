class Lesson:
    def __init__(self, classNo, startTime, endTime, weeks, venue, day, lessonType, size, covidZone, moduleCode):
        self.classNo = classNo
        self.startTime = startTime
        self.endTime = endTime
        self.weeks = weeks
        self.venue = venue
        self.day = day
        self.lessonType = lessonType
        self.size = size
        self.covidZone = covidZone
        self.moduleCode = moduleCode

    def __str__(self):
        return self.moduleCode + " (" + self.lessonType + ")"

    def purinto(self):
        print("Class No: ")
        print(self.classNo)
        print("Start time: ")
        print(self.startTime)
        print("End time: ")
        print(self.endTime)
        print("Weeks: ")
        print(self.weeks)
        print("Venue: ")
        print(self.venue)
        print("Day: ")
        print(self.day)
        print("LessonType: ")
        print(self.lessonType)
        print("Size: ")
        print(self.size)
        print("CovidZone: ")
        print(self.covidZone)
        print("ModuleCode: ")
        print(self.moduleCode)
        

class Module:
    def __init__(self, moduleCode):
        self.moduleCode = moduleCode
        self.lecture_list = [] ## array of Lesson class of all lectures
        self.tutorial_list = [] ## array of Lesson class of all tutorials

    def addLecture(self, lesson):
        self.lecture_list.append(lesson)

    def addTutorial(self, lesson):
        self.tutorial_list.append(lesson)

    def removeLecture(self, lesson):
        self.tutorial_list.remove(lesson)

    def removeTutorial(self, lesson):
        self.tutorial_list.remove(lesson)

    def __str__(self):
        return self.moduleCode

    def pint(self):
        for i in self.lecture_list:
            i.purinto()
            print("----------------------")
        for i in self.tutorial_list:
            i.purinto()
            print("-------------------------")

class Parameters:
    ## Lunch timing is pre adjusted in the timeList
    def __init__(self, startTimeList, endTimeList, timeBetween, lessonMode, dayFree):
        self.startTimeList = startTimeList ## array of integers of all starting times
        self.endTimeList = endTimeList ## array of integers of all ending times (numbers in startTimeList +1)
        self.timeBetween = timeBetween ## int of hours between each lesson
        self.lessonMode = lessonMode ## string of either online, f2f, both
        self.dayFree = dayFree ## day of the week that wants to be kept free  

class Timetable:
    def __init__(self):
        self.timetable = []
        nullLesson = Lesson("", 0, 0, [], "", "", "None", "", "", "")
        for days in range(5):
            sub_array = []
            for hours in range(10):
                sub_array.append(nullLesson)
            self.timetable.append(sub_array)

    def __str__(self):
        string = ""
        for days in self.timetable:
            for hours in days:
                string += "|"
                string += str(hours)
                string += " "
            string += "|\n" 
        return string



