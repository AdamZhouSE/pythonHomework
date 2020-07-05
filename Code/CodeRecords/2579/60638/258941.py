m=int(input())
matrix=[]
p=[]
for x in range(0,m):
    matrix.append(list(map(int,input().split(","))))
    p.append([0]*len(matrix[0]))
n=len(matrix[0])
maxN=int(input())
for i in range(0,m):
    for j in range(0,n):
        if i==0:
            if j!=0:
                p[i][j]=p[i][j-1]+matrix[i][j]
            else:
                p[i][j]=matrix[i][j]
        else:
            if j ==0:
                p[i][j]=p[i-1][j]+matrix[i][j]
            else:
                p[i][j]=p[i-1][j]+p[i][j-1]-p[i-1][j-1]+matrix[i][j]
i=min(n,m)
find=False
while i>0:
    for j in range(i-1,m):

        for k in range(i-1,n):
            if j==i-1 and k==i-1:
                if p[j][k]<=maxN:
                    find=True
                    break
                else:
                    continue
            if j==i-1:
                if p[j][k]-p[j][k-i]<=maxN:
                    find=True
                    break
                else:
                    continue
            if k==i-1:
                if p[j][k]-p[j-i][k]<=maxN:
                    find=True
                    break
                else:
                    continue
            if p[j][k]-p[j-i][k]-p[j][k-i]+p[j-i][k-i]<=maxN:
                find=True
                break
        if find:
            break
    if find:
        break
    i=i-1
print(i)