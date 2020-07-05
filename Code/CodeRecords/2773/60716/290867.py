def findRoad(x:int,y:int,path:list):
    path.append([x,y])
    if path not in paths:paths.append(path)
    if x!=0:
        if [x-1,y] not in path and lists[x][y]<lists[x-1][y]:
            t = path.copy()
            findRoad(x-1,y,t)
    if x!=height-1:
        if [x+1,y] not in path and lists[x][y]<lists[x+1][y]:
            t = path.copy()
            findRoad(x+1,y,t)
    if y!=0:
        if [x,y-1] not in path and lists[x][y]<lists[x][y-1]:
            t = path.copy()
            findRoad(x,y-1,t)
    if y!=length-1:
        if [x,y+1] not in path and lists[x][y]<lists[x][y+1]:
            t = path.copy()
            findRoad(x,y+1,t)
lists = list()
input()
temp = input()
lens = len(temp)
templist = list(eval(temp[0:lens-1]))
lists.append(templist)
for i in range(len(templist)-2):
    temp = input()
    templist = list(eval(temp[0:lens-1]))
    lists.append(templist)
templist = list(eval(input()))
lists.append(templist)
#input finished, process start
paths = list()
length = len(lists[0])
height = len(lists)
for i in range(height):
    for j in range(length):
        findRoad(i,j,[])
maxs = 0
for i in paths:
#    print(i)
    if len(i)>maxs:
        maxs = len(i)
print(maxs)