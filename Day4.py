import re


def readData(file):
    llist = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            llist.append(line.rstrip('\n'))
            #llist.append(reverse_xmas(line.rstrip('\n')))
    #llist.append(up_down_xmas(llist))
    return llist

def reverse_xmas(x):
  return x[::-1]

def up_down_xmas(xs):
    # 12345
    # 12345
    # 12345
    print("updownxmas")
    new_lines = []
    print(xs)
    reversed = [list(y) for y in zip(*xs)]
    for x in reversed:

    print(reversed)
    #for x in xs:
    #    reversed = [list(y) for y in zip(*x)]
    #    print(reversed)
    #    #new_lines.append([list(y) for y in zip(*x)])
    #print("up down lines = " + str(new_lines))
    #new_lines.append(reverse_xmas(new_lines))
    #print("up down lines reversed = " + str(new_lines))
    return new_lines

def checkforxmas(line):
    count = 0
    # count how many times xmas in this line and return that count
    reg1 = 'XMAS'
    matches = re.compile('(%s)' % (reg1)).findall(line)
    return len(matches)

if (__name__ == "__main__"):
    print("Part Test Start")
    myInput1 = readData('D4TData.txt')
    print("Part Test Input Rows = " + str(myInput1))
    columns = up_down_xmas(myInput1)
    print("Part Test Input Columns = " + str(columns))
    xmas_count = 0
    #
    for lines in myInput1:
        xmas_count = xmas_count + checkforxmas(lines)
    print("Part Test Safe Report Count = " + str(xmas_count))

    print("Part 1 Real Data")
