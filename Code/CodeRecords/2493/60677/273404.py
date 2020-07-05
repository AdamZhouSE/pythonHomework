def getTreeMin(i,treeList):
    i = int(i)
    limit = treeList.__len__()
    if i * 2 + 2 < limit:
        if treeList[i] not in answer:
            answer.append(treeList[i])
        getTreeMin(i*2+1,treeList)
        getTreeMin(i * 2 + 2, treeList)
    if i * 2 + 1 < limit:
        if treeList[i] not in answer:
            answer.append(treeList[i])
        getTreeMin(i*2+1,treeList)
    else:
        if treeList[i] not in answer:
            answer.append(treeList[i])
        return
n=int(input())
nums=input().split()
time=int(input())
answer=[]
for i in range(time):
    line=input().split()
    begin=int(line[0])-1
    end=int(line[1])
    temp=nums[begin:end]
    getTreeMin(0, temp)
    print(answer.__len__())
    answer=[]