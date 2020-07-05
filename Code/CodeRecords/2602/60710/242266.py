def findLength(A, B):
    n1 = len(A)
    n2 = len(B)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
    return max(max(row) for row in dp)
if __name__ == '__main__':
    A=eval(input())
    B=eval(input())
    re=findLength(A,B)
    print(re)