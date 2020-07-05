


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
    sizeList = input().split()
    aList = input().split()
    bList = input().split()
    stringOver = ''.join(aList + bList)
    stringOver = cleanMission(stringOver)
    print(len(stringOver))
