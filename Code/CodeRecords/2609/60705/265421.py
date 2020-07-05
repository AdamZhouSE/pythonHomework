n = int(input())
for i in range(0, n):
    [length, k] = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    i = 0
    while i < len(arr):
        element = arr[i]
        if arr.count(element) > 1:
            j = 0
            while j < len(arr):
                if arr[j] == element:
                    arr.pop(j)
                    j -= 1
                j += 1
            i = -1
        i += 1
    if k > len(arr):
        print(-1)
    else:
        print(arr[k-1])

