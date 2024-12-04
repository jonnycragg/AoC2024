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

def getmatrix(test):
    #test = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10', '11', '12']]
    #test = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']
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
    all_lines_rev = []
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
    for lines in all_lines:
        xmas_count = xmas_count + checkforxmas(lines)
    for lines in all_lines_rev:
        xmas_count = xmas_count + checkforxmas(lines)
    print("xmas count = " + str(xmas_count))
    return all_lines

if (__name__ == "__main__"):
    print("Part Test Start")
    myInput1 = readData('D4TData.txt')
    getmatrix(myInput1)
    print("Part 1 Real Data")
    myInput1 = readData('D4Data.txt')
    getmatrix(myInput1)
