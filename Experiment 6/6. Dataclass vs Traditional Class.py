from dataclasses import dataclass

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


@dataclass
class StudentData:
    name: str
    age: int


s1 = Student("Aneesha", 23)
s2 = StudentData("Aneesha", 23)

print("Traditional Class:", s1.name, s1.age)
print("Dataclass:", s2.name, s2.age)