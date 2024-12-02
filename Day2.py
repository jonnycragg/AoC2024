def readData(file):
    reports = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            llist = line.split()
            nlist = []
            for x in llist:
                nlist.append(int(x))
            reports.append(nlist)
    return reports

def checksafe(reportInput):
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    if reportInput[0] == reportInput[1]:
        return False
    increasing = True
    if reportInput[1] < reportInput[0]:
        increasing = False
    for i in range(len(reportInput)-1):
        if reportInput[i] == reportInput[i+1]:
            return False
        if abs(reportInput[i] - reportInput[i+1]) > 3:
            return False
        if increasing:
            if reportInput[i] > reportInput[i+1]:
                return False
        if not increasing:
            if reportInput[i] < reportInput[i+1]:
                return False
    return True

if (__name__ == "__main__"):
    print("Part Test Start")
    myInput1 = readData('D2TData.txt')
    print("Part Test Input = " + str(myInput1))
    safe_report_count = 0
    for report in myInput1:
        safe = checksafe(report)
        if safe:
            safe_report_count = safe_report_count + 1
            continue
        for x in range(len(report)):
            new_report = report.copy()
            new_report.pop(x)
            safe = checksafe(new_report)
            if safe:
                safe_report_count = safe_report_count + 1
                break
    print("Part Test Safe Report Count = " + str(safe_report_count))

    print("Part 1 Start")
    myInput1 = readData('D2Data.txt')
    print("Part 1 Input = " + str(myInput1))
    safe_report_count = 0
    for report in myInput1:
        safe = checksafe(report)
        if safe:
            safe_report_count = safe_report_count + 1
            continue
        for x in range(len(report)):
            new_report = report.copy()
            new_report.pop(x)
            safe = checksafe(new_report)
            if safe:
                safe_report_count = safe_report_count + 1
                break
    print("Part 1 Safe Report Count = " + str(safe_report_count))
