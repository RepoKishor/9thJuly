"""This example demonstrates Inheritance
    This class is the Parent class
"""
class student:
    def __init__(self):
        self.name="kishor"
        self.qual="grad"
        print("Initializing Parent class.....")
    def details(self):
        print("name::",self.name)
        print("age::",self.qual)

class fsdsstudent(student):
    def __init__(self):
        super().__init__()
        print("Intializing the fsds child class")


fsds=fsdsstudent()
fsds.details()