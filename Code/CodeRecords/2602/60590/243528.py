import ast
A = ast.literal_eval(input())
B = ast.literal_eval(input())

def findLength(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    # 用dp[i][j] 表示 A[:i]和B[:j]的解
    dp = [[0 for _ in range(len(B) + 1)] for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
    return max([max(row) for row in dp])

print(findLength(A,B))