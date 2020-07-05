arrA=eval(input())
arrB=eval(input())
maxs=0
dp=[[0]*(len(arrA)+1) for i in range(len(arrB)+1)]
for i in range(len(arrB)):
    for j in range(len(arrA)):
        if arrB[i]==arrA[j]:
            dp[i+1][j+1]=dp[i][j]+1
            maxs=max(dp[i+1][j+1],maxs)
print(maxs)