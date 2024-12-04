import re


def readData(file):
    llist = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            llist.append(line.rstrip('\n'))
            #llist.append(reverse_xmas(line.rstrip('\n')))
    #llist.append(up_down_xmas(llist))
    return llist

def reverse_xmas(xl):
    revlist = []
    for x in xl:
        revlist.append(x[::-1])
    return revlist

def up_down_xmas(xs):
    # 12345
    # 12345
    # 12345
    print("updownxmas")
    new_lines = []
    print(xs)
    reversed = [list(y) for y in zip(*xs)]
    for x in reversed:
        new_lines.append(''.join(x))
    print(new_lines)
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
    rows_rev = reverse_xmas(myInput1)
    columns_rev = reverse_xmas(columns)
    print("Part Test Input Columns Reversed = " + str(columns_rev))
    print("Part Test Input Rows reversed = " + str(rows_rev))
    xmas_count = 0
    for lines in myInput1:
        xmas_count = xmas_count + checkforxmas(lines)
    print("Part Test xmas Count Rows = " + str(xmas_count))
    for lines in columns:
        xmas_count = xmas_count + checkforxmas(lines)
    print("Part Test xmas Count Cols = " + str(xmas_count))
    for lines in rows_rev:
        xmas_count = xmas_count + checkforxmas(lines)
    print("Part Test xmas Count Rows reversed = " + str(xmas_count))
    for lines in columns_rev:
        xmas_count = xmas_count + checkforxmas(lines)
    print("Part Test xmas Count Cols reversed = " + str(xmas_count))

    print("Part 1 Real Data")
