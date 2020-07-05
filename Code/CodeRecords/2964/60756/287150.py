def dp(A:list,B:list)->int:
    m=len(A)
    n=len(B)
    if m==0:return n
    if n==0:return m
    DP=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(n+1):
        DP[0][i]=i
    for i in range(m+1):
        DP[i][0]=i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1]==B[j-1]:
                DP[i][j]=DP[i-1][j-1]
            else:
                DP[i][j]=min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])+1
    return DP[m][n]

N=int(input())
arr=[]
ans=[]
for i in range(N):
    arr.append(list(input()))
for i in range(N):
    for j in range(i+1,N):
        ans.append(dp(arr[i],arr[j]))
for i in range(1,9):
    print(ans.count(i),end=" ")