import bisect
arr=sorted(list(map(int,input().split(","))))
target=int(input())
n=len(arr)
prefix=[0]
for i in range(n):
    prefix.append(prefix[-1]+arr[i])
r,ans,diff=max(arr),0,target
for i in range(1,r+1):
    insert=bisect.bisect_left(arr,i)
    cur=prefix[insert]+(n-insert)*i
    if abs(cur-target)<diff:
        ans,diff=i,abs(cur-target)
print(ans)