def findKthNumber( m, n, k):
    """
    :type m: int
    :type n: int
    :type k: int
    :rtype: int
    """
    if k == 1:
        return 1
    if k == m * n:
        return m * n

    left = 0
    right = m * n

    while left < right:
        middle = (left + right) // 2
        tmp = sub(m, n, middle)

        if tmp < k:
            left = middle + 1
        else:
            right = middle

    return left


def sub( m, n, mid):
    cnt = 0
    for i in range(1, m + 1):
        cnt += min(mid // i, n)

    return cnt

m = int(input())
n = int(input())
k = int(input())
print(findKthNumber(m,n,k))