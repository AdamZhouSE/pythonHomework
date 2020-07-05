arr=input().split(',')
t=int(input())
#arr=int(arr)
arr = [ int(x) for x in arr ]
arr.sort()
l=0
r=arr[-1]
ln=len(arr)
ans=1000000
res=1000000
while l<=r:
    mid=int((l+r)/2)
    tmp=0
    i=0
    while i<ln and arr[i]<=mid:
        tmp+=arr[i]
        i+=1
    tmp+=(ln-i)*mid
    if abs(ans-t)>abs(tmp-t): 
        ans=tmp
        res=mid
    if abs(ans-t)==abs(tmp-t): res=min(res,mid)
    if tmp>t: r=mid-1
    if tmp<=t: l=mid+1
print(res)
#print(arr[0])