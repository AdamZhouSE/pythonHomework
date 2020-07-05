import re
title = input()
pattern = re.compile('[a-z]')
a = pattern.findall(title)
tar = input()
left = 0
right = len(a) - 1
res = None
while left <= right:
    mid = (left + right)//2
    if a[mid] > tar:
        res = a[mid]
        right = mid - 1
    else:
        left = mid + 1
if res is None and len(a) > 0:
    res = a[0]
print(res)
