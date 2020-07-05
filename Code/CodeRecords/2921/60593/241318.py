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
mid=s[(len(s)+1)//2]
for i in range(len(s)):
    if((s[i]-mid)%d!=0):
        ans=False
    else:
        cnt+=(abs(mid-s[i]))//d
print(cnt if ans else -1)