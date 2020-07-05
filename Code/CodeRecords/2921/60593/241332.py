n,m,d=map(int,input().split())
s=[]
for i in range(n):
    temp=map(int,input().split())
    for j in temp:
        s.append(j)
s.sort()
ans=True
cnt=0
mid=s[n*m//2 if (n*m)%2==0 and n*m>1 else (n*m+1)//2]
for i in range(len(s)):
    if(abs(s[i]-mid)%d!=0):
        ans=False
    else:
        cnt+=abs(mid-s[i])//d
print(cnt if ans else -1)