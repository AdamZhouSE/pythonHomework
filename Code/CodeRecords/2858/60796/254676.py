n=int(input())
s=[None]*n
ls=[]
for i in range(n):
    ls.append(s)
for i in range(n):
    for j in range(n):
        if i==0 of j==0:
            ls[i][j]=1
        else:
            ls[i][j]=ls[i-1][j]+ls[i][j-1]
print(ls[n-1][n-1])