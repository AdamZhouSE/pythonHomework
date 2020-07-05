testNum=int(input())
for i in range (testNum):
    srcs=input().split(' ')
    size=int(srcs[0])
    num = int(srcs[1])
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    exist=False
    items.sort()
    for s in range(size-1):
        for t in range(s+1,size):
            if(items[s]*items[t]==num):
                exist=True
    if(exist): print('Yes')
    else:print('No')