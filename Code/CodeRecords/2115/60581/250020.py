import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

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
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
                str += lst[i][j]
            else:
                judgeWord = False
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

def subDFS(v):
    isVisited[v] = 1
    for i in range(len(picture)):
        if i!=v and picture[v][i]!=0:
            if isVisited[i]==1 and father[v] != i:
                temp = v
                ring = []
                while temp != i:
                    ring.append(temp+1)
                    temp = father[temp]
                ring.append(temp+1)
                ringList.append(ring)
            else:
                if isVisited[i]==0:
                    father[i] = v
                    subDFS(i)
    isVisited[v] = -1

def DFS():
    for i in range(len(picture)):
        if isVisited[i]== 0 :
            subDFS(i)


testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    pointNumbers = input[start][0]
    sideNumbers = input[start][1]
    sides = input[start+1:start+sideNumbers+1].copy()
    picture = [[-1 for i in range(pointNumbers)]for i in range(pointNumbers)]
    father = [0]*pointNumbers
    isVisited = [False]*pointNumbers
    ringList = []
    judge = False
    for i in range(sideNumbers):
        point1 = sides[i][0]
        point2 = sides[i][1]
        picture[point1-1][point2-1] = 1
        picture[point2-1][point1-1] = 1
    DFS()
    print(ringList)
    for i in range(len(ringList)):
        if len(ringList[i])%2==1:
            judge = False
    if sideNumbers >= pointNumbers + 2:
        judge = False
    if judge:
        print("YES")
    else:
        print("NO")
        


    count += 1
    start += sideNumbers + 1
