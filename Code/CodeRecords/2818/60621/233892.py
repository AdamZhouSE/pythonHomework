temp=list(input().split())
n,t=int(temp[0]),int(temp[1])
tota=[int(x) for x in input().split()]
tota.sort()
ans=0
for time in tota:
    ans+=time*t
    if(t>1):
        t-=1
print(ans)