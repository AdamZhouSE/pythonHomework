A=input()[1:-1].split(',')
A=[int(x) for x in A]
B=input()[1:-1].split(',')
B=[int(x) for x in B]
n1 = len(A)
n2 = len(B)
dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
print(max(max(row) for row in dp))
