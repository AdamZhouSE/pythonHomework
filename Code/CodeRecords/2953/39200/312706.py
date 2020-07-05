def search(a, b, n):
    if a > n or b > n:
        return -1
    if a == n or b == n:
        return 0
    res = []
    re1 = search(a, a + b, n)
    re2 = search(a + b, b, n)
    if re1 != -1:
        res.append(re1)
    if re2 != -1:
        res.append(re2)
    if len(res) == 0:
        return -1
    return min(res)


n = int(input())
print(search(1, 1, n), end = "")
