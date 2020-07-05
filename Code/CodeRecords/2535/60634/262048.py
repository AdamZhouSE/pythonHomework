arr = eval(input())

count = 0
i = 0
while i < len(arr):
    n = arr[i]
    point = 0
    while point <= n+1:
        if point == n+1-i:
            count += 1
            i += point
            break
        if arr[i+point] > n:
            n = arr[i+point]
        point += 1
print(count)