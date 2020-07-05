testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    sum=int(input())
    exist=False
    items.sort()
    for s in range(size-3):
        for t in range(s+1,size-2):
            for m in range(t+1,size-1):
                for n in range(m+1,size):
                    if(items[s]+items[t]+items[m]+items[n]==sum):
                        exist=True
                        break
    if(exist): print('1')
    else:print('0')