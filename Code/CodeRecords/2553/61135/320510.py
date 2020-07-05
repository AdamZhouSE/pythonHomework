nodenums = int(input())
nodelist = input().split(" ")
nodelist = list(int(x) for x in nodelist)
nodeindexlist=[i for i in range(nodenums)]
times = nodenums - 1
for i in range(times):
    nownodeindex = i + 1
    reqlist = input().split(" ")
    reqlist = list(int(x) for x in reqlist)
    nowfa=reqlist[0]-1
    lOrR=reqlist[1]
    if(lOrR==0):
        nodeindexlist[nownodeindex]=nodeindexlist[nowfa]-1
    else:
        nodeindexlist[nownodeindex] = nodeindexlist[nowfa] + 1
nums=zip(nodeindexlist,nodelist)
sortednode=list(dict(sorted(nums)).values())
numlist=sortednode
dp=[1 for i in range(len(numlist))]
for i in range(len(numlist)):
    innermax=0
    for j in range(i):
        if(numlist[j]<numlist[i] and dp[j]>innermax):
            innermax=dp[j]
    dp[i]=innermax+1
print(nodenums-max(dp))