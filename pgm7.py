list1 = input("Enter first list (space separated): ").split()
list2 = input("Enter second list (space separated): ").split()
print("Lists are equal:", list1 == list2,"Common elements:", set(list1) & set(list2),"Elements only in first list:", set(list1) - set(list2),"Elements only in second list:", set(list2) - set(list1),sep="\n")
