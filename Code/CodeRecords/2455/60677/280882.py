def getSubsets(set):
    setList = []
    sumList=[]
    end=1<<set.__len__()
    for i in range(end):
        subset=[]
        for j in range(set.__len__()):
            if(i&(1<<j)):
                subset.append([j,set[j]])
        sum=0
        for j in subset:
            sum+=j[1]
        if setList.__len__()==0:
            setList.append(subset)
            sumList.append(sum)
        else:
            for j in range(setList.__len__()):
                if sum>sumList[j]:
                    sumList.insert(j,sum)
                    setList.insert(j,subset)
                    break
                if j==setList.__len__()-1:
                    sumList.append(sum)
                    setList.append(subset)
    return setList
def isConnected(bra,sub):
    branches=bra[:]
    subset=sub[:]
    isConnected=True
    nodes=[i[0] for i in subset]
    connect=[]
    for i in branches[:]:
        if (i[0] not in nodes) or (i[1] not in nodes):
            branches.remove(i)
    for i in nodes:
        isIn=False
        for j in branches:
            if i in j:
                isIn=True
                break
        if not isIn:
            isConnected=False
            break
    return isConnected
n=int(input())
index=input().split()
index=[int(x) for x in index]
branches=[]
for i in range(n-1):
    line=input().split()
    line=[int(x)-1 for x in line]
    branches.append(line)
setList=getSubsets(index)
for i in range(setList.__len__()):
    if isConnected(branches,setList[i]):
        sum=0
        for j in setList[i]:
            sum+=j[1]
        print(sum,end="")
        break