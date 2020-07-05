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
            theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    wordList = input[start].copy()
    k = input[start+1][0]
    maxLength = 0
    for i in range(len(wordList)):
        for j in range(i+1,len(wordList)+1):
            subString = wordList[i:j]
            wordStore = []
            for h in range(len(subString)):
                if wordStore.count(subString[h]) == 0:
                    wordStore.append(subString[h])
            if len(wordStore) != k:
                break
            else:
                length = j - i
                if maxLength < length:
                    maxLength = length
    print(maxLength)
    count += 1
    start += 2