import copy

def findMaxConn(t):
    global num
    w = copy.deepcopy(a)
    res = 0
    for j in range(n):
        w[t][j] = 0
        w[j][t] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if w[i][k]==1 and w[k][j]==1:
                    w[i][j] = 1
    for i in range(n):
        tmp = 0
        for j in range(n):
            if w[i][j]==1:
                tmp += 1
        res = max(res,tmp)
    num.append(res)
    return

n = int(input())
a = [[0]*n for i in range(n)]
num = []
for t in range(n-1):
    s = [int(i) for i in input().split()]
    a[s[0]-1][s[1]-1] = 1
    a[s[1]-1][s[0]-1] = 1
for i in range(n):
    findMaxConn(i)
minNum = min(num)
res = []
for i in range(n):
    if num[i]==minNum:
        res.append(str(i+1))
print(' '.join(res),end=' ')