T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = -1
    ans = True
    for i in range(n):
        if b[i] - a[i] > 0:
            diff = b[i] - a[i]
            while i < n and b[i] - a[i] == diff:
                a[i] += diff
                i += 1
            break
    print(["NO", "YES"][a == b])