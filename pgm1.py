str = input("Enter a string: ").casefold()
print((new := str[0] + str[1:].replace(str[0], "$")), new[-1] + new[1:-1] + new[0], sep="\n")
