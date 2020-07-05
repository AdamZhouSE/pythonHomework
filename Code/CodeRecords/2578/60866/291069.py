def smallestDivisor(nums, threshold):
    def ok(n):
        ans = 0
        for num in nums:
            now = num // n
            if num % n != 0:
                now += 1
            ans += now
        return ans <= threshold
    l = 1; r = max(nums)
    while ( l < r ):
        mid = (l+r) // 2
        if ok(mid):
            r = mid
        else:
            l = mid
        if (r - l ==1):
            if ok(l): return l
            return r
    return l
import re
a=input()
b=re.split(r'[\s\[\]\,]+',a)
c=[]
for x in b:
    if x.isdigit():
        c.append(x)
c=[int(x) for x in c]
print(smallestDivisor(c[0:-1],c[-1]))