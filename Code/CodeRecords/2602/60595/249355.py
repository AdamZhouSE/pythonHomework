def Test(A,B):
    dp=[]
    for i in range(0,len(A)+1):
        dp.append([])
    result=0
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            dp[i][j]=dp[i-1][j-1]+1 if(A[i-1]==B[j-1]) else 0
            result=max(result,dp[i][j])
    return result

if __name__ == "__main__":
    A=eval(input())
    B=eval(input())
    print(Test(A,B))