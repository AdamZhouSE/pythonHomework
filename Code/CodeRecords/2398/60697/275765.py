t=list(map(int,input().split(' ')))
size=t[0]
T=t[1]
res=[]

for i in range(size):
    res.append(int(input()))
leng=len(res)
def check(nums):
    lis = []
    for i in range(nums):
        lis.append(res[i])
    if(len(lis)==0):
        return False
    for i in range(nums,leng):
        tmp=min(lis)
        lis.remove(tmp)
        tmp+=res[i]
        if(tmp>T):
            return False
        lis.append(tmp)

    maxsize=max(lis)
    if(maxsize>T):
        return False
    return True
l=0
r=leng
ans=0
while(l<=r):
    mid=(l+r)//2
    if(check(mid)):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)


