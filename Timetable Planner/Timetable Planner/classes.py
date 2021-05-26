class Lesson:
    def __init__(self, classNo, startTime, endTime, weeks, venue, day, lessonType, size, covidZone):
        self.classNo = classNo
        self.startTime = startTime
        self.endTime = endTime
        self.weeks = weeks
        self.venue = venue
        self.day = day
        self.lessonType = lessonType
        self.size = size
        self.covidZone = covidZone

    def purinto(self):
        print("Class No: " + self.classNo)
        print("Start time: " + self.startTime)
        print("End time: " + self.endTime)
        print("Weeks: " + self.weeks)
        print("Venue: " + self.venue)
        print("Day: " + self.day)
        print("Lesson Type: " + self.lessonType)
        print("Size: " + self.size)
        print("Covid Zone: " + self.covidZone)

class Module:
    def __init__(self):
        self.lecture_list = []
        self.tutorial_list = []

    def addLecture(self, lesson):
        self.lecture_list.append(lesson)

    def addTutorial(self, lesson):
        self.tutorial_list.append(lesson)

    def removeLecture(self, lesson):
        self.tutorial_list.remove(lesson)

    def removeTutorial(self, lesson):
        self.tutorial_list.remove(lesson)

class Parameters:
    ## Lunch timing is pre adjusted in the timeList
    def __init__(self, startTimeList, endTimeList, timeBetween, lessonType, dayFree):
        self.startTimeList = startTimeList
        self.endTimeList = endTimeList
        self.timeBetween = timeBetween
        self.lessonType = lessonType
        self.dayFree = dayFree



