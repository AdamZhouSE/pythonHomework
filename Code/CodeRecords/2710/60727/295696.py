arr = list(map(int, input().split()))
n, q = arr[0], arr[1]
arr, res = [], []
for i in range(0, q):
    arr.append(input().split())
for i in range(0, q):
    t = arr[i]
    if t[0] == 'M':
        res.append((int(t[1]), int(t[2])))
    elif t[0] == 'D':
        ans = n + 1
        for item in res:
            if item[0] <= int(t[1]) and item[1] >= int(t[2]):
                ans = min(ans, item[1])
        print(ans if ans < n + 1 else -1)