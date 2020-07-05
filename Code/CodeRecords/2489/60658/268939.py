from bisect import *
arr = eval(input())
lower = int(input())
upper = int(input())
ans = 0
temp = 0
prefix = [0]
for i in arr:
    temp+=i
    r = bisect_right(prefix,temp-lower)
    l = bisect_left(prefix,temp-upper)
    ans+=r-l
    insort(prefix,temp)
print(ans)