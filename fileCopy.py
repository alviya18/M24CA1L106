try:
    inf = open('twinkleTwinkle.txt', 'r')
    outf = open('copyTextFile.txt', 'w')

    print("twinkleTwinkle.txt\n")
    for line in inf:
        print(line, end='')
        outf.write(line)

    inf.close()
    outf.close()

    print("\n\n\ncopyTextFile.txt\n")
    outf = open('copyTextFile.txt', 'r')
    for line in outf:
        print(line, end='')

    outf.close()

except IOError as io:
    print("File operation failed:", io)
