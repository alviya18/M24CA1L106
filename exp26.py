""" Write a program that counts odd and even numbers in a given list."""
numlist=[1,2,3,4,5,66,79]
def oddEvenCount(numlist):
    oddCount=evenCount=0
    for i in numlist:
        if not i%2:
            evenCount += 1
        else:
            oddCount += 1
    return f"\nEven numbers : {evenCount} \nOdd Numbers : {oddCount}"
print("List : ",str(numlist).strip('[]'),oddEvenCount(numlist))
