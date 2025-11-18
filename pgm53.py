#Check whether a given positive integer is power of 2. Raise exception for negative input.
try:
    num = int(input("Number ? : "))
    if num < 0:
        raise ValueError("Negative Number")
    print(num, end="")
    pow=num
    while pow%2==0 and pow//2!=1:
            pow=pow//2
    if pow//2==1:
        print(" is a power of 2")
    else :
        print(" not a power of 2")
except ValueError as e:
    print(e)
