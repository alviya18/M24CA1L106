str1,str2=input("Enter first string :"),input("Enter second string :")
print(f"{str2[0]+str1[1:]} {str1[0]+str2[1:]}")
colours=input("Enter the colours seperated by comma : ").split(",")
print(colours[::2])