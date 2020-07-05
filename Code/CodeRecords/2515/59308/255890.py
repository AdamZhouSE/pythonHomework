import re
pattern = re.compile('[0-9]+')
a = [int(x) for x in pattern.findall(input())]
m = int(input())
left = max(a)
ans = sum(a)
right = sum(a)
while left < right:
    count = 1
    mid = (left+right)//2
    s = 0
    for i in range(len(a)):
        if s + a[i] > mid:
            count += 1
            s = a[i]
        else:
            s += a[i]
    if count <= m:
        ans = mid
        right = mid
    else:
        left = mid + 1
print(ans)


