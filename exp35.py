# Find the lengthiest line in a file
try:
    file = open('twinkleTwinkle.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line, end='')
    lines.sort(key=len, reverse=True)
    print('\n\nThe lengthiest line is:', lines[0])

except IOError as e:
    print("File operation failed:", e)

finally:
    file.close()
