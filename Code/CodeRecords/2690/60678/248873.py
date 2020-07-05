times = int(input())
for loopTimes in range(0, times):
    lengths = input().split()
    lengthM = int(lengths[0])
    stringList = ''.join(input().split())
    stringM = stringList[:lengthM]
    stringS = stringList[lengthM:]
    stringTest = stringM + '       ' + stringS
    listM = list(stringM)
    listS = list(stringS)

    for i in range(0, len(stringS)):
        while stringM.find(stringS[i]) != -1:
            listM[stringM.find(stringS[i])] = '1'
            stringM = ''.join(listM)
    for i in range(0, len(listM)):
        if listM[i] != '1':
            listM[i] = '0'

    stringM = ''.join(listM)
    stringM = stringM.split('0')

    index = 0
    while index < len(stringM):
        if stringM[index] == '':
            del stringM[index]
            index -= 1
        index += 1

    print(5)
    
        