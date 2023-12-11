from abc import ABCMeta, abstractclassmethod

class IPersion(metaclass=ABCMeta):

    @abstractclassmethod
    def person_method():
        ''' Interface Method'''

class Student(IPersion):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_method(self):
        print ("student do somthing")

class Teacher(IPersion):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_method(self):
        print ("teacher do somthing")

class PersonFactory:
    @staticmethod
    def create_person(person_type):
        if(person_type == "student"):
            return Student("student", 18)
        elif(person_type == "teacher"):
            return Teacher("teacher", 32)
        else:
            print ("Invalid Type")
            return -1

# s1 = Student("tom", 14)
# s1.person_method()

# t1 = Teacher("ann", 32)
# t1.person_method()
if __name__ == "__main__":
    create_type = "student" # student, teacher
    person = PersonFactory.create_person(create_type)
    person.person_method()