testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:
        items.append(int(rawInput))
    haveMiss=False
    haveRepeat=False
    miss=[]
    repeat=[]
    for n in range(1,size+1):
        tmp=items.count(n)
        if(tmp>1):
            haveRepeat=True
            repeat.append(n)
            break
    printRepeat=0
    if(haveRepeat): printRepeat=max(repeat)
    for m in range(1 ,size+1):
        if(m not in items):
            haveMiss=True
            miss.append(m)
            break
    printMiss=0
    if(haveMiss):printMiss=max(miss)
    ans=[]
    ans.append(printRepeat)
    ans.append(printMiss)
    print(' '.join(str(s)for s in ans))