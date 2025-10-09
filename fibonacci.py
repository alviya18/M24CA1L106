limit,a,b=int(input("Enter the limit : ")),0,1
fibonacciSeries=[0,1]
if limit<0:
    print("Number is negative cannot compute fibonacci series!")
else:
    print(a,b,sep="\n")
    for i in range(2,limit):
        c = a + b
        a=b
        b=c
        print(c)
        fibonacciSeries.append(c)
an=int(input("Enter position : "))
print("element in position ",an," is",fibonacciSeries[an-1],"\nSum of the list : ",sum(fibonacciSeries))
