S=list(input())
s=[]

for i in S:
    s.append(ord(i))
print(s)
k=int(input())
res=[]
res.append(s)
for i in range(len(s)):
    print(res)
    y=max(s[:k+1])
    s.append(y)
    s.pop(s.index(y))
    res.append(s)
res.sort()
ans=""
print(S)
print(k)
print(s)
print(res)
for i in res[0]:
    ans=ans+chr(i)
print(ans)