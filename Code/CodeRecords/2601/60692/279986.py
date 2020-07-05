m = int(input())
n = int(input())
k = int(input())
l, r = 0, m * n


def count(x):
    cnt = 0
    for i in range(1, m + 1):
        cnt += min(x // i, n)
    return cnt >= k


while l < r:
    mid = (l + r) // 2
    if count(mid):
        r = mid
    else:
        l = mid + 1
print(l)