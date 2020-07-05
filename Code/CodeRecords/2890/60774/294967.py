import copy

def isLine(Pos0,Pos1,Pos2):
    x0 = Pos0[0]
    y0 = Pos0[1]
    x1 = Pos1[0]
    y1 = Pos1[1]
    x2 = Pos2[0]
    y2 = Pos2[1]
    return (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0)

s = input().split(' ')
n = int(s[0])
Pos0 = [int(s[1]),int(s[2])]
posLst = []
count = 0
for i in range(0,n):
    s = input().split(' ')
    posLst.append([int(s[0]),int(s[1])])
while(len(posLst) != 0):
    temp = []
    Pos1 = posLst[0]
    for Pos2 in posLst:
        if(not isLine(Pos0,Pos1,Pos2)):
            temp.append(Pos2)
    posLst = copy.deepcopy(temp)
    count = count + 1
print(count)