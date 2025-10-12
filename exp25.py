"""Write a program that count the number of strings where string length is 2 or more and the first and last characters are same."""
str=input("Enter the string : ")
def strLength(string):
    return len(string) if string[0].lower() == string[-1].lower() else "Cannot Provide Length"
print( strLength(str) if len(str)>=2 else "")