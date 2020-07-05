f=[[0 for i in range(100)] for i in range(100)]
root=[[0 for i in range(100)] for i in range(100)]

def pre_print(l,r):
    if l>r:
        return
    print(root[l][r],end=" ")
    if l==r:
        return
    pre_print(l,root[l][r]-1)
    pre_print(root[l][r]+1,r)

if __name__=='__main__':
    n=int(input())
    point=list(map(int, input().split(" ")))
    for i in range(0,n):
        f[i+1][i+1]=point[i]
        root[i+1][i+1]=i+1
    for l in range(1, n):
        i=1
        while i+l<=n:
            j=i+l
            f[i][j]=f[i+1][j]+f[i][i]
            root[i][j]=i
            for k in range(i+1,j):
                if f[i][j]<f[i][k-1]*f[k+1][j]+f[k][k]:
                    f[i][j] = f[i][k - 1] * f[k + 1][j] + f[k][k]
                    root[i][j]=k
            i+=1
    print(f[1][n])
    pre_print(1,n)