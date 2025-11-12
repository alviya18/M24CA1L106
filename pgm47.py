#Create a class Person with private attributes name and age. Compare 2 Persons by their age.
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __eq__(self,other):
        return self.__age==other.__age

    def __lt__(self,other):
        return self.__age<other.__age

    def __gt__(self,other):
        return self.__age>other.__age

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"

p1=Person("Aleena",20)
p2=Person("Liona",30)
print(p1)
print(p2)
if p1==p2:
    print("Both people have the same age ")
elif p1>p2:
    print("Person 1 is older than person 2")
elif p1<p2:
    print( f"Person 1 is yonger than person 2")