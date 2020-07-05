read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
low, high, mid = 0, len(ns) - 1, 0
while low + 1 < high:
    mid = (low + high) // 2
    if ns[mid] < ns[high]:
        high = mid
    elif ns[mid] > ns[high]:
        low = mid
    else:
        high -= 1
print(min(ns[low], ns[low + 1]))
