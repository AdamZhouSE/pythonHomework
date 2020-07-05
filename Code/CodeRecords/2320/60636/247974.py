S=list(input())
s=[]

for i in S:
    s.append(ord(i))
print(s)
k=int(input())
res=[]
res.append(s)
for i in range(len(s)):
    y=max(s[:k])
    s.append(y)
    s.pop(s.index(y))
    a=s.copy()
    res.append(a)
res.sort()
print(res)
ans=""
print(S)
print(k)
print(s)
for i in res[0]:
    ans=ans+chr(i)
print(ans)