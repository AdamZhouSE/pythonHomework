Max = 202000

ufs = [0 for i in range(Max)]
Id = list(ufs)
vis = list(ufs)
A = [[0, 0] for i in range(Max)]
Ring = [[] for i in range(Max)]


def find(x: int):
    if ufs[x] != x:
        ufs[x] = find(ufs[x])
    return ufs[x]


def dfs(u: int):
    if vis[u] == 0:
        Ring[recent].append(u)
        vis[u] = 1
        dfs(Id[u])


if __name__ == '__main__':
    ns = input().split()
    n = int(ns[0])
    s = int(ns[1])
    arr = input().split()
    res = []
    for i in range(1, n+1):
        A[i][0] = int(arr[i-1])
        A[i][1] = ufs[i] = i
    A = [[0, 0]] + sorted(A[1:n+1], key=lambda l: l[0])
    for i in range(1, n+1):
        Id[A[i][1]] = i
    for i in range(1, 1+n):
        if A[i][0] == A[Id[i]][0] and i != Id[i]:
            x = A[i][1]
            y = Id[i]
            A[y][1] = x
            Id[x] = y
            Id[i] = A[i][1] = i
    summary = 0
    recent = 0
    for i in range(1, n+1):
        ufs[find(i)] = find(Id[i])
    lst = 0
    for i in range(1, n+1):
        if Id[i] != i:
            summary += 1
            if lst and A[lst][0] == A[i][0] and find(A[lst][1]) != find(A[i][1]):
                ufs[find(A[lst][1])] = find(A[i][1])
                tmp = Id[A[lst][1]]
                Id[A[lst][1]] = Id[A[i][1]]
                Id[A[i][1]] = tmp
            lst = i
    for i in range(1, n+1):
        if Id[i] != i and not vis[i]:
            recent += 1
            dfs(i)
    if summary > s:
        res.append("-1")
    else:
        trn = min(s - summary, recent)
        if trn <= 2:
            res.append(recent)
            for i in range(1, recent+1):
                res.append(len(Ring[i]))
                tmp = []
                for j in Ring[i]:
                    tmp.append(j)
                res.append(tmp)
        else:
            res.append(recent - (trn - 2))
            for i in range(1, recent - trn + 1):
                res.append(len(Ring[i]))
                tmp = []
                for j in Ring[i]:
                    tmp.append(j)
                res.append(tmp)
            summary = 0
            for i in range(recent - trn + 1, recent + 1):
                sum += len(Ring[i])
            res.append(summary)
            for i in range(recent - trn + 1, recent + 1):
                tmp = []
                for j in Ring[i]:
                    tmp.append(j)
                res.append(tmp)
            res.append(trn)
            tmp = []
            for i in range(recent, recent - trn, -1):
                tmp.append(Ring[i][0])
            res.append(tmp)
    for i in res:
        if type(i) is list:
            for j in i:
                print(j, end=' ')
            print()
        else:
            print(i)