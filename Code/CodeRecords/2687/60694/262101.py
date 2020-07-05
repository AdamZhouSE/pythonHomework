def hasAlternatingBits(n):
    if n == 0: return True
    while n != 0:
        a = n & 1
        n >>= 1
        b = n & 1
        if a == b: return False
    return True


T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    for i in range(N):
        if hasAlternatingBits(i):
            ans.append(i)
    print(*ans)
