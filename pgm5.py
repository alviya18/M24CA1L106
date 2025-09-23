dict1={1:20,2:5,3:98}
dict2={4:35,6:3,8:10}
print("Dictionary items are : ", dict1, "Ascending order : ",dict(sorted(dict1.items())),"Descending order : ", dict(sorted(dict1.items(), reverse=True)),"Inverted Dictionary : " ,{v: k for k, v in dict1.items()},sep="\n")
key=int(input("Enter a key : "))
print("Key already exist : ",key in dict1)
print("Two dictionaries are : ",dict1,dict2, "Merged dictionary is : ",dict1|dict2)

