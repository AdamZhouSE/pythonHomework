import re
title = input()
pattern = re.compile('[0-9]+')
a = pattern.findall(title)
a = [int(x) for x in a]
d = int(input())
left = max(sum(a)//d - 1, max(a))
right = sum(a)
ans = 0
while left < right:
    mid = (left + right)//2
    s = 0
    c = 0
    for i in range(len(a)):
        s += a[i]
        if s > mid:
            s = a[i]
            c += 1
    c += 1
    if c <= d:
        ans = mid
        right = mid
    else:
        left = mid + 1

print(ans)



