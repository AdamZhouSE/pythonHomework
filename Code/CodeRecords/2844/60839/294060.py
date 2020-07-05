lis=list(map(int,input().split(" ")))
n=lis[0]
t=lis[1]
lis1=list(map(int,input().split(" ")))

ans=0
i=0
while t>0 and i<len(lis1):
    if t>=lis1[i]:
        t=t-lis1[i]
        ans=ans+1
    i=i+1
print(ans)