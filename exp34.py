#Write a pgm to remove a line from a specific position from a file
try:
    file = open('twinkleTwinkle.txt', 'r')
    for line in file:
        print(line, end='')
    file.close()

    pos = int(input("\n\nPosition of line to remove? : "))

    with open('twinkleTwinkle.txt', 'r+') as file:
        lines = file.readlines()
        lines.pop(pos - 1)
        file.seek(0)
        file.truncate()
        file.writelines(lines)

    with open('twinkleTwinkle.txt', 'r') as file:
        print("\n\nNew File:\n")
        for line in file:
            print(line, end='')

except IOError as io:
    print("File operation failed:", io)

