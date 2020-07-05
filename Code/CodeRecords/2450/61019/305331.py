read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]
ns = read_line()
n = read()
low, high, mid = 0, len(ns) - 1, 0
while low < high:
    mid = (1 + low + high) // 2
    if ns[mid] >= n:
        high = mid - 1
    else:
        low = mid
else:
    mid = low
    r1 = mid + 1 if ns[mid + 1] == n else -1
low, high = 0, len(ns) - 1

while low < high:
    mid = (low + high) // 2
    if ns[mid] <= n:
        low = mid + 1
    else:
        high = mid
else:
    mid = low
    r2 = mid - 1 if ns[mid - 1] == n else -1

print([r1, r2])
