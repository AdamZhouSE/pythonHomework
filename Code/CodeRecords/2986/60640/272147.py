"""
字符串1进行删除，插入，替换到字符串2
"""


def distance(source, target):
    global dp
    # 如果target为空，只需要将source全部删去
    if len(target) == 0:
        return len(source)
    # 如果source为空，只需要进行len(target)此插入操作即可
    if len(source) == 0:
        return len(target)
    # 初始化第一列 
    for i in range(0, len(source)+1):
        dp[i][0] = i
    # 初始化第一行
    for i in range(0, len(target)+1):
        dp[0][i] = i
    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
    return dp[len(source)][len(target)]


str1 = input()
str2 = input()
count = 0
# 初始化二维数组
dp = [[0 for col in range(len(str2)+1)] for row in range(len(str1)+1)]
print(distance(str1, str2))
