# Count the number of lines in a file
try:
    file = open('twinkleTwinkle.txt', 'r')
    for line in file:
        print(line, end='')
    lines=file.readlines()
    print('\n\nNo: of line : ',len(line))
    file.close()
except IOError as io:
    print("File operation failed:", io)


