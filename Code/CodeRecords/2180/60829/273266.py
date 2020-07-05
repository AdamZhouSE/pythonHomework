a = input()
b = input()
if len(a) > len(b):
    a, b = b, a
res = 0
d = {}
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        t = a[i:j]
        if t in d.keys():
            d[t][0] += 1
        else:
            d[t] = [1, 0]
for i in range(len(b)):
    for j in range(i+1, len(b)+1):
        t = b[i:j]
        if t in d.keys():
            d[t][1] += 1
for i, j in d.values():
    res += i*j
print(res, end='')