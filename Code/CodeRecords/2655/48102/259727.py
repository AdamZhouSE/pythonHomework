def search(num: int) -> int:
    table = [2**i for i in range(31)]
    left = 0
    right = 30
    while left < right:
        mid = (left + right) >> 1
        if table[mid] >= num:
            right = mid
        else:
            left = mid + 1
    return table[left]


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(search(n))
for j in res:
    print(j)