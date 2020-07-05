def numSquares(n):
    q = list()
    q.append([n, 0])
    visited = [False for _ in range(n + 1)]
    visited[n] = True
    while any(q):
        num, step = q.pop(0)
        i = 1
        tnum = num - i ** 2
        while tnum >= 0:
            if tnum == 0:
                return step + 1
            if not visited[tnum]:
                q.append((tnum, step + 1))
                visited[tnum] = True
            i += 1
            tnum = num - i ** 2

n=int(input())
print(numSquares(n))