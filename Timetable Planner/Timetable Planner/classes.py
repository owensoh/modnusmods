import nusmod_api_getter as func
import operator

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
        self.lessonTypeNumber = 0

    def __str__(self):
        return " " + self.moduleCode + " (" + self.lessonType + ")"

    def __eq__(self, other):
        return self.moduleCode == other.moduleCode and self.classNo == other.classNo and self.lessonType == other.lessonType

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
        self.nullLesson = Lesson("", 0, 0, [], "", "", "None", "", "", "")
        self.lecture_list = [] ## array of Lesson class of all lectures
        self.tutorial_list = [self.nullLesson] ## array of Lesson class of all tutorials
        self.laboratory_list = [self.nullLesson]
        self.length = 0
        self.lectureClassNo = []

    def addLecture(self, lesson):
        self.lecture_list.append(lesson)
        if lesson.classNo not in self.lectureClassNo:
            self.lectureClassNo.append(lesson.classNo)

    def addTutorial(self, lesson):
        if self.tutorial_list == [self.nullLesson]:
            self.tutorial_list = []
        self.tutorial_list.append(lesson)

    def addLaboratory(self, lesson):
        if self.laboratory_list == [self.nullLesson]:
            self.laboratory_list = []
        self.laboratory_list.append(lesson)

    def removeLecture(self, lesson):
        self.lecture_list.remove(lesson)

    def removeTutorial(self, lesson):
        self.tutorial_list.remove(lesson)

    def removeLaboratory(self, lesson):
        self.laboratory_list.remove(lesson)

    def updateLength(self):
        self.length = len(self.lecture_list) + len(self.tutorial_list) + len(self.laboratory_list)

    def __str__(self):
        for i in self.lectureClassNo:
            print(i)
        return self.moduleCode 

    def pint(self):
        for i in self.lecture_list:
            i.purinto()
            print("----------------------")
        #for i in self.tutorial_list:
        #    i.purinto()
        #    print("-------------------------")
        #for i in self.laboratory_list:
        #    i.purinto()
        #    print("-------------------------")

class Parameters:
    ## Lunch timing is pre adjusted in the timeList
    def __init__(self, startTimeList, endTimeList, timeBetween, lessonMode, dayFree):
        self.startTimeList = startTimeList ## array of integers of all starting times
        self.endTimeList = endTimeList ## array of integers of all ending times (numbers in startTimeList +1)
        self.timeBetween = timeBetween ## int of hours between each lesson
        self.lessonMode = lessonMode ## string of either online, f2f, both
        self.dayFree = dayFree ## day of the week that wants to be kept free  

class Student:
    def __init__(self, moduleList, module_dict):
        self.moduleList = moduleList
        self.timetable = []
        self.nullLesson = Lesson("", 0, 0, [], "", "", "None", "", "", "")
        for days in range(5):
            sub_array = []
            for hours in range(10):
                sub_array.append(self.nullLesson)
            self.timetable.append(sub_array)
        self.days = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4}
        self.allModuleLessonList = []
        self.impossible = False
        self.module_dict = module_dict


    def __str__(self):
        string = ""
        for days in self.timetable:
            for hours in days:
                string += "|"
                string += str(hours)
                string += " "
            string += "|\n" 
        return string

    def debugTimetable(self):
        string = ""
        for days in self.timetable:
            for hours in days:
                string += "|"
                string += str(hours)
                string += " "
            string += "|\n" 
        return string

    def addLesson(self, lesson):
        for i in range(lesson.endTime - lesson.startTime):
            if self.timetable[self.days[lesson.day]][lesson.startTime + i - 8] != self.nullLesson:
                return False
        for i in range(lesson.endTime - lesson.startTime):
            self.timetable[self.days[lesson.day]][lesson.startTime + i - 8] = lesson
        return True

    def removeLesson(self, lesson):
        for i in range(lesson.endTime - lesson.startTime):
            self.timetable[self.days[lesson.day]][lesson.startTime + i - 8] = self.nullLesson


    ## Trigger print error
    def cannotGetTimetable(self):
        print("IMPOSSIBLE :'(")
        self.impossible = True

    def forceLecture(self):
        done = True
        for module in self.moduleList:
            if len(module.lectureClassNo) == 1:
                for lecture in module.lecture_list:
                    done = self.addLesson(lecture)
                    if done == False:
                        self.cannotGetTimetable()
                        break
                module.lecture_list = [self.nullLesson]
                if done == False:
                    break

    def addParam(self, param):
        new_moduleList = []
        for module in self.moduleList:
            new_moduleList.append(func.parameterise(module, module.moduleCode, param))

        for module in new_moduleList:
            module.updateLength()
        self.moduleList = sorted(new_moduleList, key=operator.attrgetter('length'))

        for module in self.moduleList:
            if module.lecture_list != [self.nullLesson]:
                self.allModuleLessonList.append(module.lecture_list)
                if module.lecture_list == []:
                    self.cannotGetTimetable()
                    print(module.moduleCode + " cannot lecture")

        for module in self.moduleList:
            self.allModuleLessonList.append(module.tutorial_list)
            if module.tutorial_list == []:
                self.cannotGetTimetable()
                print(module.moduleCode + " cannot tutorial")

        for module in self.moduleList:
            self.allModuleLessonList.append(module.laboratory_list)
            if module.laboratory_list == []:
                self.cannotGetTimetable()
                print(module.moduleCode + " cannot laboratory")



    def generate(self, param):
        copy_timetable = self.timetable.copy()
        
        def backtrack(param, allModuleLessonList):

            for i in range(len(allModuleLessonList)):
                lessonAdded = False

                
                if str(allModuleLessonList[i][0]) != str(self.nullLesson):
                    
                    #if problem_lessonType == "Laboratory":
                    #    for s in allModuleLessonList[i]:
                    #        print(s.venue)
                    for lesson in allModuleLessonList[i]:
                        day = self.days[lesson.day]
                        startTime = lesson.startTime - 8
                        endTime = lesson.endTime - 8
                        count = 1
                        possible = True
                        while count < param.timeBetween + 1:
                            tempStart = startTime - count
                            tempEnd = endTime + count - 1
                            if tempStart >= 0:
                                if self.timetable[day][tempStart] != self.nullLesson:
                                    possible = False
                                    break
                            if tempEnd <= 9:
                                if self.timetable[day][tempEnd] != self.nullLesson:
                                    possible = False 
                                    break
                            count += 1
                        if possible:
                            lessonAdded = self.addLesson(lesson)
                        
                        if lessonAdded:
                            print(lesson.moduleCode, lesson.lessonType, lesson.startTime, lesson.endTime, lesson.day)
                            print(self.debugTimetable())
                            print(i, len(allModuleLessonList) - 1)
                            
                            new_allModuleLessonList = allModuleLessonList.copy()
                            new_allModuleLessonList[i] = [self.nullLesson]
                            if backtrack(param, new_allModuleLessonList) == False:
                                self.removeLesson(lesson)
                                print(lesson.moduleCode, lesson.lessonType, lesson.startTime, lesson.endTime, lesson.day, 'yikes')
                                lessonAdded = False
                            else:
                                return True
                        else:
                            print(lesson.moduleCode, lesson.lessonType, lesson.startTime, lesson.endTime, lesson.day, 'yikes')
                else:
                    lessonAdded = True
                if lessonAdded == False:
                    return False
            #if lessonAdded:
            #    return True
            #else:
            #    self.cannotGetTimetable()
            #    print(problem_mod + " cannot cos " + problem_lessonType)
            #    return False
        if backtrack(param, self.allModuleLessonList) == False:
            print("Try again")
            self.timetable = copy_timetable
        else:
            print("yay")
            self.updateModule_dict()
            
    def updateModule_dict(self):
        for day in self.timetable:
            for hour in day:
                if hour != self.nullLesson:
                    if hour.lessonType == "Lecture":
                        self.module_dict[hour.moduleCode][0] = hour.classNo
                    elif hour.lessonType == "Tutorial":
                        self.module_dict[hour.moduleCode][1] = hour.classNo
                    elif hour.lessonType == "Laboratory":
                        self.module_dict[hour.moduleCode][2] = hour.classNo

    def generateNusmodsLink(self):
        link = "https://nusmods.com/timetable/sem-2/share?"
        lessonType_lst = ['LEC', 'TUT', 'LAB']
        for module in self.module_dict.keys():
            link += module + "="
            for i in range(len(self.module_dict[module])):
                if self.module_dict[module][i] != "":
                    link += lessonType_lst[i] + ':' + self.module_dict[module][i] + ','
            link += '&'
        return link







