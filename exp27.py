"""Write a function to get a new string from a given string by adding ‘Is’ to the beginning of the input string. If the given string already begins with ‘Is’, return the input string unchanged."""
str=input("Enter the string : ")
def newStr(string):
    if string[0:2]=="Is":
        return string
    else:
        return "Is"+string
print("New String : ",newStr(str))