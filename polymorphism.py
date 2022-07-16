"""
This is the example that demonstrates the polymorphism
The type of the object decides the version of the method being called.
"""
class dataScience:
    def __init__(self):
        print("Intializing dataScience")

    def getCourseName(self):
        print("Welcome to course of DataScience")
    def getCourseDuration(self):
        print("The course duration of Data Science is 9 months")

class bigData:
    def __init__(self):
        print("Intializing BigData")
    def getCourseName(self):
        print("Welcome to the course of Big Data")
    def getCourseDuration(self):
        print("The course duration of Big data is 3 months")

def registerForACourse(course):
    course.getCourseName()
    course.getCourseDuration()

ds=dataScience()
bd=bigData()
registerForACourse(ds)
registerForACourse(bd)