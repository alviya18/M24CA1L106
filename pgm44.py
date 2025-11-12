# Create a class Person (name, age) with a constructor and a method display().
# Create a class Employee (EmpID) from Person, override display() to include the ID.
# Create a derived class Faculty (department) from Employee, override display() to include the department.
# Create a separate class Researcher with a method can_do_research() that returns a string indicating the person can conduct research.
# Create a final class Professor which inherits from Faculty and Researcher.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"NAME : {self.name}\nAGE : {self.age}")

class Employee(Person):
    def __init__(self,name,age,EmpID):
        super().__init__(name,age)
        self.EmpId=EmpID

    def display(self):
        super().display()
        print(f"ID : {self.EmpId}")

class Faculty(Employee):
    def __init__(self,name,age,EmpID,department):
        super().__init__(name,age,EmpID)
        self.department=department

    def display(self):
        super().display()
        print(f"DEPARTMENT : {self.department}")

class Researcher:
    def can_do_research(self):
        return "This person can conduct research."

class Professor(Faculty,Researcher):
    def __init__(self, name, age, EmpID, department):
        Faculty.__init__(self, name, age, EmpID, department)

    def display(self):
        super().display()
        print(self.can_do_research())

professor=Professor("Merin",34,"P5663MT","BioTech")
professor.display()