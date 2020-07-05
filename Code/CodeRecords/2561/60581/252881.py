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
        judgeNumber = False
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
    N = input[start][0]
    x = input[start][1]
    matrixA = input[start+1:start+N+1]
    matrixB = input[start+N+1:start+2*N+1]

    stringA = []
    stringB = []
    for i in range(len(matrixA)):
        for j in range(len(matrixA[i])):
            stringA.append(matrixA[i][j])
    for i in range(len(matrixB)):
        for j in range(len(matrixB[i])):
            stringB.append(matrixB[i][j])
    totalCount = 0
    for i in range(len(stringA)):
        for j in range(len(stringB)):
            if stringA[i]+stringB[j]==x:
                totalCount += 1

    print(totalCount)
    count += 1
    start += 2 * N