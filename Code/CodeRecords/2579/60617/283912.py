def prefix_sum():
    m=int(input())
    mat=[]
    for i in range(0,m):
        arr=eval("["+input()+"]")
        mat.append(arr)
    thr=int(input())
    n=len(mat[0])
    P=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            P[i][j]=P[i-1][j]+P[i][j-1]-P[i-1][j-1]+mat[i-1][j-1]
    print(mat)

    def calRec(x1,x2,y1,y2):
        return P[x2][y2]-P[x1-1][y2]-P[x2][y1-1]+P[x1-1][y1-1]
    r,ans=min(m,n),0
    for i in range(1, m+1):
        for j in range(1, n+1):
            for c in range(ans+1, r+1):
                if i+c-1<=m and j+c-1<=n and calRec(i,j,i+c-1,j+c-1)<=thr:
                    ans+=1
                else:
                    break
    print(ans)

if __name__=='__main__':
    prefix_sum()