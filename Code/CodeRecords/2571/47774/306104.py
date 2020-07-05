n=int(input())
matrix=[]
for i in range(n):
    a=list(map(int,input().split(',')))
    matrix.append(a)
k=int(input())

m=len(matrix)
n=len(matrix[0])
dp=[[0 for i in range(n)] for j in range(m)]
dp[0][0]=matrix[0][0]
for i in range(1,m):
    dp[i][0]=dp[i-1][0]+matrix[i][0]
for i in range(1,n):
    dp[0][i]=dp[0][i-1]+matrix[0][i]
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=matrix[i][j]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]

def solve():
    ans=0
    for a in range(m):
        for b in range(a,m):
            for c in range(n):
                for d in range(c,n):
                    if a==0:
                        top=0
                    else:
                        top=dp[a-1][d]
                    if c==0:
                        left=0
                    else:
                        left=dp[b][c-1]
                
                    if a==0 or c==0:
                        lt=0
                    else:
                        lt=dp[a-1][c-1]
                    cur=dp[b][a]-left-top+lt
                    if cur==k:
                        return k
                    if cur<k:
                        ans=max(ans,cur)
    return ans                       
print(solve())               
                
                
                