import re

def readData(file):
    llist = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            llist.append(line.rstrip('\n'))
    return llist

def reverse_xmas(xl):
    revlist = []
    for x in xl:
        revlist.append(x[::-1])
    return revlist

def checkforxmas(line):
    count = 0
    # count how many times xmas in this line and return that count
    reg1 = 'XMAS'
    matches = re.compile('(%s)' % (reg1)).findall(line)
    pattern = re.compile(reg1)
    matches1 = pattern.finditer(line)
    positions = [(match.start(), match.end()) for match in matches1]
    return len(matches), positions

def checkforXmasDummy(lines):
    # search for A but skip first row, last row, first column last col
    # if found A check around to see if MAS spelled diagonally around me in X format and if so count
    # input looks like this: ['123456',
    # input looks like this:  '123456',
    # input looks like this:  '123456',
    # input looks like this:  '123456',
    # input looks like this:  '123456']
    count = 0
    # count how many times xmas in this line and return that count
    total_num_lines = len(lines)
    lcounter = -1
    ccounter = -1
    for x in lines:
        lcounter = lcounter + 1
        # ignore first and lat lines
        if lcounter == 0: continue
        if lcounter == len(lines)-1: continue
        ccounter = -1
        for y in x:
            ccounter = ccounter + 1
            # ignore first and last columns
            if ccounter == 0: continue
            if ccounter == len(x)-1: continue
            if y == 'A':
                wordl = lines[lcounter-1][ccounter-1] + y + lines[lcounter+1][ccounter+1]
                wordr = lines[lcounter+1][ccounter-1] + y + lines[lcounter-1][ccounter+1]
                if ''.join(sorted(wordl)) == ''.join(sorted(wordr)) == 'AMS':
                    count = count + 1
    print("XXMAS Dummy count of found " + str(count))
    return count

def getmatrix(test):
    max_col = len(test[0])
    max_row = len(test)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(test[y][x])
            rows[y].append(test[y][x])
            fdiag[x + y].append(test[y][x])
            bdiag[x - y - min_bdiag].append(test[y][x])

    all_lines = []
    for x in cols:
        all_lines.append(''.join(x))
    for x in rows:
        all_lines.append(''.join(x))
    for x in fdiag:
        all_lines.append(''.join(x))
    for x in bdiag:
        all_lines.append(''.join(x))
    all_lines_rev = reverse_xmas(all_lines)
    xmas_count = 0
    xmas_count_match_coords = []
    for lines in all_lines:
        count, cords = checkforxmas(lines)
        xmas_count = xmas_count + count
        xmas_count_match_coords.append(cords)
    for lines in all_lines_rev:
        count, cords = checkforxmas(lines)
        xmas_count = xmas_count + count
        xmas_count_match_coords.append(cords)
    print("xmas count = " + str(xmas_count))
    print("xmas count coords = " + str(xmas_count_match_coords))
    return all_lines

if (__name__ == "__main__"):
    print("Part Test Start")
    myInput1 = readData('D4TData.txt')
    getmatrix(myInput1)
    print("Part 2 Test Data")
    myInput1 = readData('D4TData.txt')
    checkforXmasDummy(myInput1)
    print("Part 2 Real Data")
    myInput1 = readData('D4Data.txt')
    checkforXmasDummy(myInput1)
