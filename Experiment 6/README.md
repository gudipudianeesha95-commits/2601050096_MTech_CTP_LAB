**EXPERIMENT 6 — Dataclass vs Traditional Class**

The workbook asks for a Student/Employee data model using dataclasses and comparison with a traditional class.

**Aim**

To implement a Student data model using dataclass and traditional class.

**Algorithm**

1. Create a traditional class.

2. Create a dataclass.

3. Store student information.

4. Display the information.

5. Compare both approaches.

**Python Program**

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

**Output**

Traditional Class: Aneesha 23

Dataclass: Aneesha 23

**Data & Result**

Both classes store the same student information.

**Inference & Analysis**

Dataclasses reduce the amount of code needed to create simple data models.

**Result**

Thus, a Student data model was successfully implemented and compared.
