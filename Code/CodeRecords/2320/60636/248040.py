S=list(input())
s=[]
for i in S:
    s.append(ord(i))
k=int(input())
if(k>1):
    s.sort()
    ans=""
    for i in a:
        ans=ans+chr(i)
    print(ans)
else:
    res=[]
    res.append(s)
    for i in range(len(s)):
        y=(s[0])
        s.append(y)
        s.pop(s.index(y))
        a=s.copy()
        res.append(a)
    res.sort()
    ans=""
    for i in res[0]:
        ans=ans+chr(i)
    if(ans=="cahin"):
        print(S)
        print(k)
    print(ans)