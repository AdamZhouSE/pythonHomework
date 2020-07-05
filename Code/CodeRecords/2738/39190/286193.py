import sys
def func4(matrix):
    maxarea=0
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='0':
                continue
            if j==0:
                width=dp[i][j]=1
            else:
                width=dp[i][j]=dp[i][j-1]+1
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                maxarea = max(maxarea, width * (i-k+1))
    print(maxarea)

list = []  
for line in sys.stdin:    
    list.extend(line.split())
ip=""
for item in list:
    ip=ip+item
func4(eval(ip))