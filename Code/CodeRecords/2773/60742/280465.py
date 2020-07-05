def find(i,j):
    global visited
    global len1
    if visited[i][j]:
        return len1[i][j]
    if i-1>=0 and a[i-1][j]<a[i][j]:
        len1[i][j] = max(len1[i][j],find(i-1,j)+1)
    if j-1>=0 and a[i][j-1]<a[i][j]:
        len1[i][j] = max(len1[i][j],find(i,j-1)+1)
    if i+1<n and a[i+1][j]<a[i][j]:
        len1[i][j] = max(len1[i][j],find(i+1,j)+1)
    if j+1<n and a[i][j+1]<a[i][j]:
        len1[i][j] = max(len1[i][j],find(i,j+1)+1)
    visited[i][j] = True
    return len1[i][j]

s = input()
a = []
a.append(eval(input().strip()[:-1]))
n = len(a[0])
for t in range(n-2):
    a.append((eval(input().strip()[:-1])))
a.append((eval(input().strip())))
s = input()
visited = []
len1 = []
tmp1 = []
tmp2 = []
for i in range(n):
    tmp1.append(False)
for i in range(n):
    visited.append(tmp1)
for i in range(n):
    tmp2.append(1)
for i in range(n):
    len1.append(tmp2)
res = 0
for i in range(n):
    for j in range(n):
        res = max(res,find(i,j))
print(res)