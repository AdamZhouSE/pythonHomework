def arrays_20_charge(n,a_num,b_num,arr_A=[],arr_B=[]):
    dp = [[0]* (b_num + 1) for i in range(a_num +1)]
    for i in range(1,b_num + 1):
        dp[0][i] = dp[0][i-1] +arr_B[i-1]
    for i in range(1,a_num +1):
        dp[i][0] = dp[i-1][0] +arr_A[i-1]
    for i in range(1,a_num+1):
        for j in range(1,b_num + 1):
            if i+j<=n:
                a_add = dp[i - 1][j] + arr_A[i+j-1]
                b_add = dp[i][j - 1] + arr_B[i+j-1]
                dp[i][j] = max(a_add,b_add)
            else:
                dp[i][j] = max(dp[i - 1][j],dp[i][j-1])
    print(dp[-1][-1])
if __name__=='__main__':
    for  i in range(int(input())):
        n,a_num,b_nam = map(int,input().split())
        arr_A = list(map(int,input().split()))
        arr_B = list(map(int,input().split()))
        arrays_20_charge(n,a_num,b_nam,arr_A,arr_B)