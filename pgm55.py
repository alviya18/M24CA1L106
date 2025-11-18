#Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
string="Classmate"
len=len(string)
newStr=[string[(len//2)-1:((len+1)//2)+1]]
for char in newStr:
    print(char.upper())