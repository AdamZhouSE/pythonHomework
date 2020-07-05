s=list(input())
k=int(input())
res=[]
res.append(s)
for i in range(len(s)):
    y=max(s[:k+1])
    s.append(s)
    s.pop(s.index(y))
    if(not s in res):
        res.append(s)
res.sort()
print(res[-1])