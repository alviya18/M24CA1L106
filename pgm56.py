#Arrange characters in a string such that lowercase letters must come first.
string=input("String ? :")
newStr=""
for char in string:
    if char.islower():
        newStr+=char
for char in string:
    if char.isupper():
        newStr+=char
print(newStr)
