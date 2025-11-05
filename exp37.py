class Student:
    def __init__(self, roll=0, name="", phone=""):
        self.roll = roll
        self.name = name
        self.phone = phone

    def setPhone(self, phone):
        self.phone = phone

    def getName(self):
           return self.name

    def getPhone(self):
        return self.phone

    def print(self):
        print("Roll No  : ", self.roll)
        print("Name     : ", self.name)
        print("Phone    : ", self.phone)


s = Student(1, "Alviya")
s.setPhone("7034004672")
s.print()
