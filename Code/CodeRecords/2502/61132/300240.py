t = int(input())
l=[]
ans=0
for j in range(t):
    s=int(input())
    if not l or l[-1]>s:
        l.append(s)
    else:
        while not l or l[-1]<=s:
            l.pop()
            ans+=min(l[-1],s) if not l else s
            l.append(s)
if len(l)>1:
    ans+=l[:-1]
print(ans)