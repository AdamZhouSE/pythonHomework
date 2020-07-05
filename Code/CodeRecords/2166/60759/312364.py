ts = int(input())
for t in range(ts):
    n = int(input())
    ans = [n]
    n -= 1
    while n > 0:
        ans.insert(0, n)
        t = n
        while t > 0:
            tail = ans.pop()
            ans.insert(0, tail)
            t -= 1
        n -= 1
    print(' '.join(list(map(str, ans))))
