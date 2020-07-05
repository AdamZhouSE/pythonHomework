n,m,d=map(int,input().split())
s=set()
for i in range(n):
    temp=map(int,input().split())
    for j in temp:
        s.add(j)
s=list(s)
s.sort()
ans=True
cnt=0
for i in range(1,len(s)):
    if((s[i]-s[i-1])%d!=0):
        ans=False
    else:
        cnt+=(s[len(s)-1]-s[i])//d
print(cnt if ans else -1)