arr1 = list(eval(input()))
arr2 = list(eval(input()))

n = len(arr1)
ans = 0
for dx, dy in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
    maxv = 0
    minv = 4000000
    for i in range(n):
        maxv = max(maxv, arr1[i] * dx + arr2[i] * dy + i)
        minv = min(minv, arr1[i] * dx + arr2[i] * dy + i)
        ans = max(ans, maxv - minv)
print(ans)

 