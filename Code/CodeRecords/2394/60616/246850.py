testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:items.append(int(rawInput))
    ans =[]
    for item in items:
        if(item!=0):ans.append(item)
    num=len(ans)
    for j in range(size-num):
        ans.append(0)
    print(' '.join(str(s)for s in ans),'')