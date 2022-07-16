"""
This is the demonstration of multilevel inheritance
"""

class RegisteredStudent:
    def __init__(self,name):
        self.name=name
    def getName(self):
        print("Your name is ",self.name)

class EnrolledCourse(RegisteredStudent):
    def __init__(self,name,courseName):
        RegisteredStudent.__init__(self,name)
        self.courseName = courseName

    def classType(self):
        print("You have enrolled for a course: from EnrolledCourse class", self.courseName)

class JobGuranteeProgram(EnrolledCourse):
    def __init__(self,name,courseName,jobassistance):
        EnrolledCourse.__init__(self,name,courseName)
        self.jobassistance = jobassistance

    def getProgram(self):
        print(" You have joined the jobgurantee program FSDS")

pg = JobGuranteeProgram("Kishor","FSDS","JobPreparation")
pg.getName()
pg.classType()
pg.getProgram()


