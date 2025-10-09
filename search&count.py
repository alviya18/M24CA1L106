list = [1,3,3,7,9,2,8,9,11,43,8,7,10]
val = int(input("Search Element? : "))
def find(item, numlist):
    count = 0
    for num in numlist:
        if item == num:
            count += 1
    if count == 0:
        return "Element not found!"
    else:
        times = "time" if count == 1 else "times"
        return f"Element found and occurs {count} {times}."
print(find(val, list ))
