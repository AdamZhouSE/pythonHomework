def dp(i,j):
    global f
    idx = roots.index(i)
    id = i[0]
    left = lch[idx][0]
    right = rch[idx][0]
    if j==0:
        f[id][j] = 0
    elif left==0 and right==0:
        f[id][j] = i[1]
    else:
        for k in range(j):
            if f[left][k]==0:
                dp(lch[idx],k)
            if f[right][j-k-1]==0:
                dp(rch[idx],j-k-1)
            f[id][j] = max(f[id][j],f[left][k]+f[right][j-k-1]+i[1])
    return                

n,k = [int(i) for i in input().split()]
edge1 = []
edge2 = []
weight = []
for t in range(n-1):
    s = [int(i) for i in input().split()]
    edge1.append(s[0])
    edge2.append(s[1])
    weight.append(s[2])
roots = []
lch = []
rch = []
q = []
f = [[0 for i in range(k+2)] for _ in range(n+1)]
q.append([1,0])
while q:
    tmp = q.pop(0)
    roots.append(tmp)
    if tmp[0] not in edge1 and tmp[0] not in edge2:
        lch.append([0,0])
        rch.append([0,0])
    lflag = False
    while tmp[0] in edge1:
        idx1 = edge1.index(tmp[0])
        if lflag:
            rch.append([edge2[idx1],weight[idx1]])
        else:
            lch.append([edge2[idx1],weight[idx1]])
            lflag = True
        q.append([edge2[idx1],weight[idx1]])
        edge1.pop(idx1)
        edge2.pop(idx1)
        weight.pop(idx1)
    while tmp[0] in edge2:
        idx2 = edge2.index(tmp[0])
        if lflag:
            rch.append([edge1[idx2],weight[idx2]])
        else:
            lch.append([edge1[idx1],weight[idx2]])
            lflag = True
        q.append([edge1[idx2],weight[idx2]])
        edge1.pop(idx2)
        edge2.pop(idx2)
        weight.pop(idx2)
dp([1,0],k+1)
print(f[1][k+1])