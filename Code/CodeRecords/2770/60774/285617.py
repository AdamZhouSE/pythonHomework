import copy

def getKey(inf):
    return inf[1]

t = int(input())
for i in range(0,t):
    arrange = []
    result = ''
    conf = int(input())
    startTime = list(map(int,input().strip().split(' ')))
    endTime = list(map(int,input().strip().split(' ')))
    confInf = [[s,e] for s,e in zip(startTime,endTime)]
    infCopy = copy.deepcopy(confInf)
    infCopy.sort(key = getKey)
    while(len(infCopy) > 0):
        cur = infCopy[0][1]
        arrange.append(endTime.index(cur) + 1)
        infCopy = list(filter(lambda x:x[0] > cur,infCopy))
    for j in range(0,len(arrange)):
        result = result + str(arrange[j]) + ' '
    print(result)