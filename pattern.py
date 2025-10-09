limit=int(input("Limit? : "))
for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(i,2*i):
        print(" * ",end=" ")
    print()
