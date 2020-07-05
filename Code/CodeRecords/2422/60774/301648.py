import copy

def mov(oriLst):
    newLst = []
    tempLst = copy.deepcopy(oriLst)
    for i in range(1,len(oriLst),2):
        newLst.append(oriLst[i])
        tempLst.remove(oriLst[i])
    return newLst + tempLst

def locate(cur,lst):
    location = cur + 1
    while(location < len(lst)):
        if(lst[location] > lst[cur]):
            break
        else:
            location = location + 2
    return location - 2

n = int(input())
numLst = list(map(int,input().split(' ')))
cur = 0
count = 0
step = []
while(cur < len(numLst)):
    loc = locate(cur,numLst)
    if(loc < cur):
        cur = cur + 1
    else:
        step.append([cur + 1,loc + 1])
        numLst = numLst[:cur] + mov(numLst[cur:loc + 1]) + numLst[loc + 1:]
        count = count + 1
        cur = 0
print(count)
for item in step:
    print(item[0],item[1])