"""Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list. """
numlist=[1,11,23,2,7,8,98,7,84,8,9,237,22,20]
def even(list):
    evenlist = []
    for i in list:
        if i == 237:
            break
        if not i%2:
            evenlist.append(i)
    return str(evenlist).strip("[]")
print("List : ",str(numlist).strip('[]'),"\nEven Numbers : ",even(numlist))