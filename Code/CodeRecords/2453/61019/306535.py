read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split(',')]

ns = read_line()
n = read()
low, high, mid = 0, len(ns) - 1, 0
while low <= high:
    mid = (low + high) // 2
    if n == ns[mid]:
        print(True)
        exit(0)
    elif ns[mid] < ns[high]:
        if ns[mid] < n <= ns[high]:
            low = mid + 1
        else:
            high = mid - 1
    elif ns[mid] > ns[high]:
        if ns[mid] > n > ns[low]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        high -= 1
print(False)
