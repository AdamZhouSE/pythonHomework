[n, q] = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
dic = {}
for qi in range(0, q):
    [li, ri] = list(map(int, input().split(" ")))
    for j in range(li, ri+1):
        dic.setdefault(j, 0)
        dic[j] += 1

so = sorted(dic.items(), key=lambda k: k[1], reverse=True)
arr.sort()
arr.reverse()
res = 0
for i in range(0, len(so)):
    res += so[i][1] * arr[i]
print(res)
