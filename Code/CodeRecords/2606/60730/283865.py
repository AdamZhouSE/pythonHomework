m = eval(input())
target = int(input())
left, right = 0, len(m) - 1
while left <= right:
    pivot = left + (right - left) // 2
    if m[pivot] == target:
        print(pivot)
        exit()
    if target < m[pivot]:
        right = pivot - 1
    else:
        left = pivot + 1
print(-1)
