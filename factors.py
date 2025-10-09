num=int(input("Number? : "))
print("Factors are : ")
for i in range(1,num+1):
    if not num%i:
        print(i)

