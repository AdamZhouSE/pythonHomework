m = int(input())
n = int(input())
k = int(input())
left, right = 1, m*n
while left <= right:
    mid = (left + right)//2
    s = 0
    for i in range(1, m+1):
        s += min(mid//i, n)
    if s < k:
        left = mid + 1
    elif s > k:
        right = mid
    else:
        print(mid)
        break