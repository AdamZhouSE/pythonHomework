m=int(input())
n=int(input())
matrix=[]
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)
#print(matrix)
k=int(input())
for i in range(k):
    s=input()
    sl=s.split(',')
    a=int(sl[0])
    b=int(sl[1])
    for r in range(m):
        for c in range(n):
            if(r<a and c<b):
                matrix[r][c]=matrix[r][c]+1
y=0
for l in matrix:
    if(max(l)>y):
        y=max(l)
co=0
for l in matrix:
    co=co+l.count(y)
#print(matrix)
print(co)