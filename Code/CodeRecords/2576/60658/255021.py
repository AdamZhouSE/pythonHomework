def upper_bound(li,x):
    l,r = 0,len(li)
    while l<r-1:
        mid = (l+r)//2
        if li[mid]>x:
            r = mid
        else:
            l = mid
    return l

def check(x):
    return sum(x if num >= x else num for num in arr)


arr = [int(x) for x in input().split(",")]
target = int(input())
n = len(arr)
arr.sort()
prefix = [0]
for num in arr:
    prefix.append(prefix[-1]+num)
l,r,ans = 0,max(arr)+1,0
while l<r-1:
    mid = (l+r)//2
    it = upper_bound(arr,mid)
    cur = prefix[it]+(n-it)*mid
    if cur<=target:
        ans = mid
        l = mid
    else:
        r = mid

small = check(ans)
big = check(ans+1)
if abs(small-target)>abs(big-target):
    ans = ans+1
print(ans)