nums = [int(x) for x in input().split()]
n, m = nums[0], nums[1]
a = [int(x) for x in input().split()]
a.sort()
b = [int(x) for x in input().split()]
c = [0] * m
for i in range(m):
    left = 0
    right = n - 1
    mid = (left + right) // 2
    temp = b[i]
    while left <= right:
        if a[mid] <= temp:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    c[i] = left
print(' '.join([str(x) for x in c]))