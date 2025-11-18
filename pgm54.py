#Find the sum of even valued terms in a Fibonacci series.
limit,a,b=int(input("Enter the limit : ")),0,1
fibonacciSeries=[0,1]
if limit<0:
    print("Number is negative cannot compute fibonacci series!")
else:
    print(a,b,sep=" ",end=" ")
    for i in range(2,limit):
        c = a + b
        a=b
        b=c
        print(c,end=" ")
        fibonacciSeries.append(c)
    print()
print("Even values in the series :",end=" ")
sum=0
for num in fibonacciSeries:
    if not num%2:
        sum+=num
        print(num,end=", ")
print("\nSum of even values in the series : ",sum)
