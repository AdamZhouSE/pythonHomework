from bisect import *
arr = eval(input())
lower = int(input())
upper = int(input())
ans = 0
temp = 0
prefix = [0]
for i in arr:
    temp+=i
    r = bisect_right(arr,temp-lower)
    l = bisect_left(arr,temp-upper)
    ans+=max(r-l,0)
    insort(prefix,temp)
print(ans)