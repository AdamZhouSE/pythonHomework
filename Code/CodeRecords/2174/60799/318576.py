import sys


def add(alist, i, j, w):
    alist[i].append((j, w))
    alist[j].append((i, w))


def dele(alist, i, j):
    for ii in range(len(alist[i])):
        if alist[i][ii][0] == j:
            alist[i].pop(ii)
            break
    for jj in range(len(alist[j])):
        if alist[j][jj][0] == i:
            alist[j].pop(jj)
            break
    return alist


def find(alist, s, t, n):
    visi = [False] * n
    inde = [i for i in range(n)]
    minl = [sys.maxsize] * n
    visi[s] = True
    for i in alist[s]:  # start
        if minl[i[0]] > i[1]:
            minl[i[0]] = i[1]
            inde[i[0]] = 0

    res = 0
    for ttt in range(n - 1):
        mindis = sys.maxsize
        indexx = -1
        for iii in range(0, n):
            if not visi[iii]:
                if minl[iii] < mindis:
                    indexx = iii
                    mindis = minl[iii]
        res += minl[indexx]
        visi[indexx] = True

        for iii in alist[indexx]:
            if not visi[iii[0]]:
                if max(minl[indexx], iii[1]) < minl[iii[0]]:  # 不是最短路的啊 改一点点这里吧
                    minl[iii[0]] = max(minl[indexx], iii[1])
                    inde[iii[0]] = indexx
    print(minl[t] if minl[t] < sys.maxsize else -1)


inp = input().split()
n, m = int(inp[0]), int(inp[1])
alist = [[] for i in range(n + 2)]
for zz in range(m):
    inp = [int(i) for i in input().split()] + [0]
    c, i, j, w = inp[0], inp[1], inp[2], inp[3]
    if c == 0:
        add(alist, i, j, w)
    elif c == 1:
        dele(alist, i, j)
    else:
        find(alist, i, j, n)
