def findIndex(string, character):
    return string.find(character)


def cleanMission(string):
    index = 0
    string = list(string)
    while index < len(string):
        tempChar = string[index]
        indexInner = index + 1
        while indexInner < len(string):
            if string[indexInner] == tempChar:
                del string[indexInner]
                indexInner -= 1
            indexInner += 1
        index += 1
    return ''.join(string)


times = int(input())
for loopTimes in range(0, times):
    stringM = input()
    stringS = input()
    stringS = cleanMission(stringS)
    stringM =  cleanMission(stringM)
    positions = []
    positionFirst = findIndex(stringM, stringS[0])
    for i in range(0, len(stringS)):
        tempPosition = findIndex(stringM, stringS[i])
        if positionFirst > tempPosition and tempPosition != -1:
            positionFirst = tempPosition
    print(stringM[positionFirst])