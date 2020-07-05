n = int(input())
l = list(map(int, input().split(" ")))
d = {}
res = "YES"
for i in range(0, n):
    d.setdefault(l[i], 0)
    d[l[i]] += 1
# print(d)
# print(len(d))
if len(d) > 3:
    res = "NO"
if len(d) == 3:
    k = list(d.keys())
    k.sort()
    # print(k)

    if d[k[2]] != d[k[0]]:
        res = "NO"
    if k[2] - k[1] != k[1] - k[0]:
        res = "NO"
if len(d) == 2:
    # print(d)
    k = list(d.keys())
    if d[k[0]] != d[k[1]]:
        res = "NO"
    if abs(k[0] - k[1]) % 2 == 1:
        res = "NO"
print(res)