a=input()
b=input()
n,m=len(a),len(b)
D=[[0]*(n+1) for i in range(m+1)]
for i in range(1,n+1):
    D[0][i]=i
for i in range(1,m+1):
    D[i][0]=i
for i in range(1,m+1):
    for j in range(1,n+1):
        D[i][j]=min(min(D[i-1][j]+1,D[i][j-1]+1),(D[i-1][j-1]if a[j-1]==b[i-1]else D[i-1][j-1]+1))
print(D[m][n])