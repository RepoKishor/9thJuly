"""
Multiple Inheritance
"""


class iNeuronCourse:

    def getYourName(self):
        print("Hello ", self.name)

    def getQualification(self):
        print("Your qualification:", self.qualification)

    def getYrsofExp(self):
        print("Your total yrs of experience:", self.yrsofexp)

    def getCourseName(self):
        print("You have enrolled for the course:", self.coursename)


class Company:
    def getBlog(self):
        print("You can write a blog here about your experience with iNeuron")

    def getAffiliate(self):
        print("You can become an affiliate and earn rewards here")

    def getJobGurantee(self):
        print("Join the job gurantee program with us")


class Quicklinks:
    def getInternship(self):
        print("Choose the domain in which you want to do an internship and you can do multiple projects as well")

    def getVision(self):
        print("Go through the vision of iNeuron")


class iNeuronStudent(iNeuronCourse, Company, Quicklinks):
    def __init__(self, name, qualification, yrsofexp, coursename):
        self.name = name
        self.qualification = qualification
        self.yrsofexp = yrsofexp
        self.coursename = coursename

    def getFeedback(self):
        print("Please provide your valuable feedback which helps us to improve. Thank you.")


student = iNeuronStudent("kishor", "PG", "12", "FSDS")
student.getYourName()
student.getQualification()
student.getYrsofExp()
student.getCourseName()
student.getBlog()
student.getAffiliate()
student.getJobGurantee()
student.getInternship()
student.getVision()
student.getFeedback()