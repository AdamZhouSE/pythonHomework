A=list(map(int,list(eval(input()))))
B=list(map(int,list(eval(input()))))
dp = [[0 for _ in range(len(B) + 1)] for i in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
print(max([max(row) for row in dp]))
