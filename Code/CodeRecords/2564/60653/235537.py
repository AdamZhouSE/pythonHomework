import re;

s = [int(n) for n in re.findall(r"\d+", input())]
k = int(input())
x = int(input())
a = list([0]*len(s))
res = list([])
for i in range(0, len(s)):
    a[i] = s[i] - x

left = 0
if a.count(0) >= k:
    res = list([x]*k)
elif a.count(0) > 0:
    res = list([x]*a.count(0))
    left = k - a.count(0)
else:
    left = k
tag = 1
while left > 0:
    if - tag in a:
        if a.count(-tag) >= left:
            for i in range(0, left):
                res.append(x-tag)
            break
        else:
            for i in range(0, a.count(-tag)):
                res.append(x-tag)
            left -= a.count(-tag)
    if tag in a:
        if a.count(tag) >= left:
            for i in range(0, left):
                res.append(x+tag)
            break
        else:
            for i in range(0, a.count(tag)):
                res.append(x+tag)
            left -= a.count(tag)
    tag += 1
res.sort()
print(res)
