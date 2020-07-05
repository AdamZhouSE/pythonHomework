def find_max_difference(numList):
    temp = numList[0]
    dif = 0
    if len(numList) >= 2:
        dif = numList[1] - numList[0]
        if len(numList) > 2:
            for i in range(2, len(numList)):
                temp = numList[i]-numList[i-1]
                if temp > dif:
                    dif = temp
    return dif

rawList = input()[1:-1].split(',')
myList = []
for i in range(len(rawList)):
    myList.append(int(rawList[i]))
myList.sort()
print(find_max_difference(myList))