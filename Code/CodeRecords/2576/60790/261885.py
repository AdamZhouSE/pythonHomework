import bisect
arr=input().split(",")
arr=list(map(int,arr))
target=int(input())
arr.sort()
n=len(arr)
prefix=[0]
for num in arr:
    prefix.append(prefix[-1]+num)
l,r,ans=0,max(arr),-1
while(r>=l):
    mid=(r+l)//2
    it=bisect.bisect_left(arr,mid)
    cur=prefix[it]+(n-it)*mid
    if(target>=cur):
        ans=mid
        l=mid+1
    else:
        r=mid-1
def check(x):
    return  sum(x if num>=x else num for num in arr)
c_small=check(ans)
c_big=check(ans+1)
print(ans if abs(c_small - target) <= abs(c_big - target) else ans + 1)