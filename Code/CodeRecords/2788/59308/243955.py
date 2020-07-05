import re

n = int(input())
pattern = re.compile('-*[0-9]+')
a = [int(x) for x in pattern.findall(input())]
m = int(input())
b = [int(x) for x in pattern.findall(input())]
a.sort()
b.sort()
res = 0
i = 0
j = 0
while i < n and j < m:
    if abs(a[i]-b[j]) <= 1:
        i += 1
        j += 1
        res += 1
    else:
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
print(res)


