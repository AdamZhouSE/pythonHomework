def findKthNumber(m, n, k):
    lo, hi = 1, m*n
    while lo <= hi:
        mid = (lo + hi) >> 1
        loc = countLower(m,n, mid)
        if loc < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

def countLower(m,n, num):
    i, j = 1,n
    cnt = 0
    while i <= m and j >= 1:
        if i*j <= num:
            cnt += j
            i += 1
        else:
            j -= 1
    return cnt
m=int(input())
n=int(input())
k=int(input())
print(findKthNumber(m,n,k))