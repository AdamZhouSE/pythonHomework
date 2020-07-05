lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            while judgeWord:
                if j + 1 == len(lst[i]):
                    theLine.append(str)
                    break
                if (lst[i][j+1] >= 'A' and lst[i][j+1] <= 'Z') or (lst[i][j+1] >= 'a' and lst[i][j+1] <= 'z'):
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeWord = False
                    theLine.append(str)

        elif lst[i][j]>='0' and lst[i][j]<='9' or lst[i][j]=='-':
            judgeNumber = True
            str += lst[i][j]
            while judgeNumber:
                if j + 1 == len(lst[i]):
                    theLine.append(int(str))
                    break
                if lst[i][j+1] >= '0' and lst[i][j+1] <= '9':
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeNumber = False
                    theLine.append(int(str))
        j += 1
    input.append(theLine)

optNum = input[0][0]
options = input[1:]

stringList = []

for i in range(len(options)):
    if options[i][0]==1:
        stringList.insert(0,options[i][1])
        stringList.sort()
    elif options[i][0]==2:
        stringList.remove(options[i][1])
    elif options[i][0]==3:
        for j in range(len(stringList)):
            if stringList[j] == options[i][1]:
                print(j+1)
                break
    elif options[i][0]==4:
        print(stringList[options[i][1]-1])
    elif options[i][0]==5:
        maxNum = 0
        needed = options[i][1]
        for j in range(len(stringList)):
            if stringList[j]>maxNum and stringList[j]<needed:
                maxNum = stringList[j]
        print(maxNum)
    elif options[i][0]==6:
        minNum = pow(10,8)
        needed = options[i][1]
        for j in range(len(stringList)):
            if stringList[j]<minNum and stringList[j]>needed:
                minNum = stringList[j]
        print(minNum)
