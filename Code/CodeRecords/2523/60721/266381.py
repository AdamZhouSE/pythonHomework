s=input().split("],[")
s[0]=s[0].strip("[")
s[len(s)-1]=s[len(s)-1].strip(']')
lis=[list()]*len(s)
for i in range(0,len(s)):
    lis[i]=s[i].split(",")
for i in range(0,len(lis)):
    for j in range(0,len(lis[0])):
        lis[i][j]=int(lis[i][j])
def diagonalSort( mat):
    if not mat or not mat[0]:
        return None
    m, n = len(mat), len(mat[0])
    for j in range(n):
        i, l, pos = 0, [], []
        while i < m and j < n:
            l.append(mat[i][j])
            pos.append([i, j])
            i += 1
            j += 1
        l.sort()
        for i, p in enumerate(pos):
            x, y = p
            mat[x][y] = l[i]
    for i in range(1, m):
        j, l, pos = 0, [], []
        while i < m and j < n:
            l.append(mat[i][j])
            pos.append([i, j])
            i += 1
            j += 1
        l.sort()
        for i, p in enumerate(pos):
            x, y = p
            mat[x][y] = l[i]
    return mat



print(diagonalSort(lis))