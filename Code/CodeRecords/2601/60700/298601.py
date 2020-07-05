m = int(input())
n = int(input())
k = int(input())
l = 1
r = m*n
while l < r:
    mid = (l + r) // 2
    count = 0
    for i in range(1, m+1):
        count += min(mid//i, n)
    if count < k:
        l = mid + 1
    else:
        r = mid
print(l)
