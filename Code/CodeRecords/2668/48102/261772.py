def search(num: int) -> int:
    table = [2**i-1 for i in range(1, 32)]
    left = 0
    right = 31
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
    n2 = search(n)
    res.append([n2 - n, n2])
for i in res:
    print(str(i[0]) + ' ', end='')
    print(i[1])
    