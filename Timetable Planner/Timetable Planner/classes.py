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

    def getHi(self):
        print("hi")

class Module:
    def __init__(self):
        self.lesson_list = []

    def addLesson(self, lesson):
        self.lesson_list.append(lesson)



