import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

number = lst[0]
wholeCount = 0
beginNumber = 1
while wholeCount < int(lst[0]):
    First = lst[beginNumber].split()
    numberOfWord = int(First[0])
    beginWord = First[1]
    matrix = [[0 for i in range(numberOfWord + 1)] for i in range(numberOfWord)]
    WordList = lst[beginNumber + 1].split()
    for i in range(0, numberOfWord):
        matrix[i] = lst[beginNumber + 2 + i].split();
    answer = []
    count = 0
    answer.append(beginWord)
    while len(answer) < numberOfWord:
        for i in range(0, numberOfWord):
            if answer[count] == matrix[i][0]:
                for j in range(0, numberOfWord+1):
                    if matrix[i][j] == '1':
                        if answer.count(matrix[j-1][0]) == 0 :
                            answer.append(matrix[j-1][0])
                        matrix[i][j] = '0';
                        matrix[j-1][i+1] = '0';
        count += 1;
    print(" ".join(answer))
    beginNumber = beginNumber + numberOfWord + 2
    wholeCount += 1