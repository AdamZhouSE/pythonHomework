a = [int(x) for x in input().split(',')]
res = list()
d = a[1] - a[0]
flag = True
for i in range(2, len(a)):
    if a[i] - a[i-1] == d:
        if flag:
            res.append(i-2)
            flag = False
    if a[i] - a[i-1] != d:
        d = a[i] - a[i - 1]
        if not flag:
            res.append(i-1)
            flag = True
if a[len(a)-1] - a[len(a)-2] == d and not flag:
    res.append(len(a)-1)
s = 0
for i in range(1, len(res), 2):
    l = res[i] - res[i-1] + 1
    for j in range(3, l+1):
        s += l - j + 1

print(s)

