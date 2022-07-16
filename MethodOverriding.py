"""This is the demonstration for method overriding"""


class myCourse:
    def __init__(self):
        __courseName = "DataScience"
        __courseDuration = "9 months"

    def getCourseName(self):
        print("The course name is DataScience")

    def getCourseDuration(self):
        print("the course duration is 9 months")


class bigdata(myCourse):
    def getCourseDuration(self):
        print("the duration for BigData course is 3months ")


bd = bigdata()
bd.getCourseDuration()
bd.getCourseName()