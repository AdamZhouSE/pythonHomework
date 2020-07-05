read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]
ns = read_line()
n = read()
low, high = 0, len(ns) - 1
while low <= high:
    mid = (low + high) // 2
    if ns[mid] == n:
        print(mid)
        break
    if ns[mid] < ns[high]:
        if ns[high] >= n >= ns[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        if ns[low] <= n <= ns[mid]:
            high = mid - 1
        else:
            low = mid + 1
else:
    print(-1)
