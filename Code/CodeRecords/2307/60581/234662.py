import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

number = lst[0]
wholeCount = 0
beginNumber = 1
while wholeCount < int(number):
    answer = []
    numberOfList = int(lst[beginNumber])
    numberList = lst[beginNumber+1].split()
    for i in range(0,len(numberList)) :
        if numberList.count(numberList[i]) >= numberOfList/2 :
            if answer.count(numberList[i])==0 :
                answer.append(numberList[i])
    if len(answer) == 0:
        answer.append(-1)
    print(int(answer[0]))
    beginNumber += 2
    wholeCount += 1

