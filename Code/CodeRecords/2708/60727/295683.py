def exp(res: dict, arr, room):
    val = set()
    for key in res.keys():
        if res[key] == room:
            val.add(key)
    if val in arr:
        return 0
    else:
        arr.append(val)
        return len(val)
arr1 = list(map(int, input().split()))
n, m, q = arr1[0], arr1[1], arr1[2]
arr1, res, arr2 = [], {}, []
for i in range(0, q):
    arr1.append((input().split()))
for i in range(1, n + 1):
    res[i] = 1
for i in range(0, q):
    t = arr1[i]
    if t[0] == 'C':
        res[int(t[1])] = int(t[2])
    elif t[0] == 'W':
        ans = 0
        for j in range(int(t[1]), int(t[2]) + 1):
            ans += exp(res, arr2, j)
        print(ans)