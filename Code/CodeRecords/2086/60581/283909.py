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

n = input[0][0]
m = input[0][1]
road = input[1:]

visited = [1]
outPut = 0
choseRoad = []
while len(visited)<n:
    minLength = -1
    for i in range(len(road)):
        if minLength == -1 or road[i][2]<minLength:
            for j in range(len(visited)):
                if (visited[j]==road[i][0] and visited.count(road[i][1])==0) :
                    minLength = road[i][2]
                    anotherPoint = road[i][1]
                elif (visited[j]==road[i][1] and visited.count(road[i][0])==0):
                    minLength = road[i][2]
                    anotherPoint = road[i][0]
    outPut += minLength
    visited.append(anotherPoint)

print(outPut)