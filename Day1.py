def readData(file):
    startlist = []  # Declare an empty list
    endlist = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            llist = line.split()
            startlist.append(int(llist[0]))
            endlist.append(int(llist[1]))
    return startlist, endlist

if (__name__ == "__main__"):
    myInput1, myInput2 = readData('D1Data.txt')
    sInput1 = sorted(myInput1)
    sInput2 = sorted(myInput2)
    answer = 0
    for num1, num2 in zip(sInput1, sInput2):
        answer = answer + abs(num2 - num1)
    print("Part 1 Answer = " + str(answer))

    similarity_score = 0
    for num1 in myInput1:
        similarity_score = similarity_score + (num1 * myInput2.count(num1))
    print("Part 2 Answer = " + str(similarity_score))