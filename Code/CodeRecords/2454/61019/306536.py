read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
low, high, mid = 0, len(ns) - 1, 0
while low + 1 < high:
    mid = (low + high) // 2
    if ns[mid] < ns[high]:
        high = mid
    else:
        low = mid
print(min(ns[low], ns[low + 1]))
