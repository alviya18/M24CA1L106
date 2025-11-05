import re
with open('phno.txt', 'r') as file:
    lines=file.readlines()
    for line in lines:
        print(line,end='')
    key = re.compile(r'^[6-9]\d{9}$')
    print("\n\nThe data with valid phno's are : \n")
    print('Name       Address         Phno\n---------------------------------------')
    for line in lines:
        parts = line.split()
        phone = parts[-1]
        if key.match(phone):
            print(line,end='')
