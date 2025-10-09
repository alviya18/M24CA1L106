num,fact=int(input("Number? : ")),1
if num<0:
    print(num ,"is a negative number.Cannot find factorial!")
else:
    for i in range(1,num+1):
        fact*=i
    print("Factorial of ",num," is : ",fact)
