def isOK(s1:str,s2:str):
    # len(s1)<=len(s2)
    if len(s2)!=len(s1)+1:
        return False
    isMet=False
    for i in range(len(s1)):
        if s1.count(s1[i])==s2.count(s1[i]):
            continue
        if s1.count(s1[i])==s2.count(s1[i])-1 and not isMet:
            isMet=True
        else:
            return False
    return True


def findMax(dp,arr:list):
    if not len(arr):
        return [0,-1]
    maxDP,maxi=0,-1
    for i in arr:
        if dp[i]>maxDP:
            maxDP=dp[i]
            maxi=i
    return [maxDP,maxi]

from collections import defaultdict
words=[]
wordsLen=defaultdict(list)
try:
    while True:
        inp=input()
        words.append(inp)
        wordsLen[len(inp)].append(inp)
except EOFError:
    pass
words=sorted(set(words),key=lambda x:len(x))
n=len(words)
pre=defaultdict(list)
for i in range(n-1,-1,-1):
    curlen=len(words[i])
    if wordsLen.get(curlen-1) is None:break
    else:
        for x in wordsLen[curlen-1]:
            if isOK(x,words[i]):
                pre[words[i]].append(words.index(x))

dp=[1 for _ in range(n)]
before=[-1 for _ in range(n)]
for i in range(1,n):
    arr=findMax(dp,pre[words[i]])
    dp[i]=arr[0]+1
    before[i]=arr[1]

maxChain=max(dp)
print(maxChain)
idx=dp.index(maxChain)
res=[]
while idx!=-1:
    res.append(words[idx])
    idx=before[idx]
res.reverse()
for s in res:
    print(s)