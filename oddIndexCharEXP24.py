"""Write a program to remove all odd indexed characters from a given string."""
str=input("Enter the string: ")
def oddIndexCharString(string):
    return string[::2]
print(oddIndexCharString(str))
