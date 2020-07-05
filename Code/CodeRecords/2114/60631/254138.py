def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    q = list()
    q.append([n, 0])
    visited = [False for _ in range(n+1)]
    visited[n] = True
    while any(q):
        num, step = q.pop(0)
        i = 1
        tNum = num - i**2
        while tNum >= 0:
            if tNum == 0:
                return step + 1
            if not visited[tNum]:
                q.append((tNum, step + 1))
                visited[tNum] = True
            i += 1
            tNum = num - i**2
print(numSquares(int(input())))
