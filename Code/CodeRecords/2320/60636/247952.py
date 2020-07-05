S=list(input())
s=[]
for i in S:
    s.append(ord(i))
k=int(input())
res=[]
res.append(s)
for i in range(len(s)):
    y=max(s[:k+1])
    s.append(y)
    s.pop(s.index(y))
    if(not s in res):
        res.append(s)
res.sort()
ans=""
print(k)
for i in res[0]:
    ans=ans+chr(i)
print(ans)