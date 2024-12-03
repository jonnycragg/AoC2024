import re

def readData(file):
    reports = []  # Declare an empty list
    with (open(file, 'rt') as myfile):  # Open lorem.txt for reading text.
        line = myfile.read()
        reg1 = 'mul\(\d{1,3},\d{1,3}\)'
        reg2 = 'don\'t\(\)'
        reg3 = 'do\(\)'
        matches = re.compile('(%s|%s|%s)' % (reg1, reg2, reg3)).findall(line)
        do = True
        for x in matches:
            if x[0:3] == 'don':
                do = False
                continue
            if x[0:3] == 'do(':
                do = True
                continue
            if do:
                operation = x[0:3]
                operands = x[4:len(x)-1].split(",")
                reports.append([operation, operands])
    return reports

if (__name__ == "__main__"):
    print("Part Test Start")
    myInput1 = readData('D3TData.txt')
    print("Part Test Input = " + str(myInput1))
    answer = 0
    for calc in myInput1:
        operation = calc[0]
        operands = calc[1]
        answer = answer + (int(operands[0]) * int(operands[1]))
    print("Part Test answer = " + str(answer))

    print("Part 1 Start")
    myInput1 = readData('D3Data.txt')
    print("Part 1 Input = " + str(myInput1))
    answer = 0
    for calc in myInput1:
        operation = calc[0]
        operands = calc[1]
        answer = answer + (int(operands[0]) * int(operands[1]))
    print("Part Test answer = " + str(answer))
