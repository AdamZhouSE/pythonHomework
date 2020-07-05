n = int(input())
arr = list(map(int, input().split(" ")))
m = 1
for i in range(0, n):
    current = 1
    j = i + 1
    while j < n:
        if arr[j-1] < arr[j] <= 2*arr[j-1]:
            current += 1
            if current > m:
                m = current
        else:
            break
        j += 1
print(m)