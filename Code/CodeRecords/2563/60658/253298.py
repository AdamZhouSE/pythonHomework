import math
n = int(eval(input()))
ans = 0
for i in range(int(math.log(n,2)),0,-1):
    l = 1
    r = int(n**(1/(i-1))+1)
    mid = 0
    s=0.0
    while l<r-1:
        mid = (l+r)//2
        s = (mid**i-1)//(mid-1)
        if s == n:
            ans = mid
            print(ans)
            exit()
        elif s<n:
            l = mid
        else:
            r = mid
print("")