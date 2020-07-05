def numSimilarGroups(A) -> int:

    n, m = len(A), len(A[0])

    def check(x, y):
        t = 0
        for i in range(m):
            if x[i] != y[i]:
                t += 1
                if t > 2:
                    return False
        return t == 2

    p = {i: {i} for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] is not p[j]:
                if check(A[i], A[j]):
                    p[i] |= p[j]
                    for k in p[j]:
                        p[k] = p[i]
    ans = {id(p[i]) for i in p}
    return len(ans)

x=input()
x=x[2:len(x)-2]
lis=x.split("\",\"")

print(numSimilarGroups(lis))