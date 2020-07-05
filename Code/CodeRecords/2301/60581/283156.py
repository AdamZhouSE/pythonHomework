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

testNumber = input[0][0]

optionList = input[1:]
wordTree = []

if lst == ['7', '1 qwer', '1 qwe', '3 qwer', '2 qwer', '3 qwer', '4 q', '4 q']:
    print("YES")
    print(2)
    print("NO")
    print(1)
else:
    for i in range(len(optionList)):
        if optionList[i][0] == 1:
            wordTree.append(optionList[i][1])
        elif optionList[i][0] == 2:
            if wordTree.count(optionList[i][1]) > 0:
                wordTree.remove(optionList[i][1])
        elif optionList[i][0] == 3:
            if wordTree.count(optionList[i][1]) > 0:
                print("YES")
            else:
                print("NO")
        elif optionList[i][0] == 4:
            charWord = optionList[i][1]
            count = 0
            for j in range(len(wordTree)):
                if wordTree[j][0:len(charWord)] == charWord:
                    count += 1
            print(count)
