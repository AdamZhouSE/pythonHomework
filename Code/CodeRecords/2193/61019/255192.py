def simi(mid):
    if mid == 0:
        return True
    temp = {}
    for f in events:
        try:
            seg = f[-mid:]
            temp[seg] = temp[seg] + 1 if seg in temp else 1
        except IndexError:
            pass
    for v in temp.values():
        if v >= 2:
            return True
    return False


n, m = [int(x) for x in input().split(' ')]
s = input()
frac = [s[:loc + 1] for loc in range(n)]
for _ in range(m):
    l, r = [int(x) for x in input().split(' ')]
    events = frac[l - 1:r]

    low, high, res = 0, n, 0
    while low <= high:
        mid = low + (high - low) // 2
        if simi(mid):
            res = max(res, mid)
            low = mid + 1
        else:
            high = mid - 1
    print(res)
