muda=input()
matrix=[]
while True:
    c=input()
    if c==']':
        break
    if c[len(c)-1]==',':
        c=eval(c[:len(c)-1])
    else:
        c=eval(c[:len(c)])
    matrix.append(c)
area=0
width=0
dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='1':
            if j!=0:
                dp[i][j]=dp[i][j-1]+1
            else:
                dp[i][j]=1
            width=dp[i][j]
        else:
            continue
        k=i
        while k>=0:
            width=min(width,dp[k][j])
            area=max(area,width*(i-k+1))
            k-=1
print(area)