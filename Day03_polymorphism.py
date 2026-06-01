class Person:
    def __init__(self, name):
        self.name = name

    def Homework(self):
        print(f"{self.name} homework")

class Teacher(Person):
    def Homework(self):
        print(f"{self.name} give homework")

class Student(Person):
    def Homework(self):
        print(f"{self.name} do homework")


teacher1 = Teacher("Anna")
student1 = Student("Albert")
teacher1.Homework()  
student1.Homework() 
