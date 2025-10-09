def singleNum(list):
    if not list:
        return ""
    return list[0] + singleNum(list[1:])
list = input("List of digits? (separated by comma): ").split(',')
print("Combined Number:", singleNum(list))
