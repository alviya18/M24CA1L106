list = input("Enter words separated by commas: ").split(",")
print("Longest word is:", max(list, key=len))
