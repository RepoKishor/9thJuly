"""This class is to demonstrate the abstraction concept using private variable"""
class student:
    __name="Kishor"
    __coursename="FSDS"
    print("Name is ", __name)
    print("course name is ", __coursename)

    def getdetails(self):
        print("Your name is:", self.__name)
        print("Your course name is", self.__coursename)
stu=student()
stu.getdetails()
print(stu.name)
print(stu.coursename)