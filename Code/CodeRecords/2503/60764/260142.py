def findLongestWay(path,ind):
    res=[]
    if ind+1>=len(path):
        return 0
    for i in range(ind+1,len(path)):
        if path[i][0]==path[ind][1]:
            res.append(1+findLongestWay(path,i))
    if len(res)==0:
        return 0
    return max(res)
n=int(input())
path=[]
for i in range(n-1):
    path.append(list(input().split()))
res=[]
i=0
while path[i][0]=='1':
    res.append(1+findLongestWay(path,i))
    i+=1
if len(res)==1:
    print(res[0])
else:
    print(res.pop(res.index(max(res)))+res.pop(res.index(max(res))))