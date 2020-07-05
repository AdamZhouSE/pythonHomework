def diagonalSort(mat):
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


s=input()
s=s[1:len(s)-1]
countL=0
count=0
countC=0
for c in s:
    if c=='[':
        countL+=1
    if c.isdigit():
        count+=1
countC=count//countL
mat=[[0 for i in range(countC)] for j in range(countL)]
i=0
j=0
while i<countL:
    for c in s:
        if c.isdigit():
            mat[i][j]=int(c)
            j=j+1
        if j==countC:
            j=0
            i=i+1
diagonalSort(mat)
print(mat)