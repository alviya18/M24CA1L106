a,b=set(map(int,(input("Enter first collection of integers : ").split()))),set(map(int,input("Enter second collection of integers : ").split()))
print("Length of both sets are same : ",len(a)==len(b))
print("The sum of both collection are same : ",sum(a)==sum(b))
print("There exists a same value in both set : ",bool(a&b))
