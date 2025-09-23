color_list1={'yellow','white','purple','violet','black','indgo','magenta', "olive", "mint", "cream", "ivory", "plum","coral", "peach", }
color_list2 = {"black", "white", "orange", "pink", "purple", "brown", "grey", "cyan", "magenta", "lavender", "turquoise", "mustard"}
print("LIST 1 : ",color_list1,"LIST 2 : ",color_list2,"Colors only in LIST 1 : ",color_list1-color_list2,sep="\n")
print("Colors in both list : ", color_list1 or color_list2)
str=set(input("Enter elements to a set:"))
print("Empty set : ",bool(not len(str)))

