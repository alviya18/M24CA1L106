def revName(name):
    if not name:
        return ""
    return name[-1] + " " + revName(name[:-1])
name = input("Full Name? : ").split()
print("Reversed Name:", revName(name).strip())
