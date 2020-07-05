n,m,d=map(int,input().split())
s=set()
for i in range(n):
    temp=list(map(int,input().split()))
    for j in temp:
        s.add(j)
s=list(s).sort()
ans=True
for i in range(1,len(s)):
    if((s[i]-s[i-1])%d!=0):
        ans=False
print(len(s)-1 if ans else -1)