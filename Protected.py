"""This class is to demonstrate the abstraction concept using protected variable"""
class student:
    _courseName="DataScience"
    _qualification="Graduation"

class fsdsStu(student):
    pass

fsds=fsdsStu()
print("trying to access protected variable coursename:", fsds.courseName)
print("trying to access protected variable qualification:", fsds.qualification)
print("accessing protected variable",fsds._courseName)
print(fsds._qualification)

"""This class is to demonstrate the abstraction concept using protected variable"""


class student1:
    _courseName = "DataScience"
    _qualification = "Graduation"


class fsdsStu(student1):

    def getDetails(self):
        print(self._courseName)
        print(self._qualification)


fsds = fsdsStu()
fsds.getDetails()