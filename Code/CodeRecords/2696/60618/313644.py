class Solution:
    def find(self, d):
        n=len(d[0])
        dp = [[1 for i in range(n)],[1 for i in range(n)],[1 for i in range(n)],[1 for i in range(n)]] # d[i][j]代表第i行选择第j个数的最长波动序列长度

        for j in range(1,n):
            for k in range(j):
                # 第1行
                for i in range(4):
                    if d[0][j]>=d[i][k]:
                        dp[0][j] = max(dp[0][j],dp[i][k]+1)
                # 第2行
                for i in range(4):
                    if d[1][j]<=d[i][k]:
                        dp[1][j] = max(dp[1][j],dp[i][k]+1)
                # 第3行
                for i in range(4):
                    if i == 3:
                        continue
                    if d[2][j]>=d[i][k]:
                        dp[2][j] = max(dp[2][j],dp[i][k]+1)
                # 第4行
                for i in range(4):
                    if i==2:
                        continue
                    if d[3][j]<=d[i][k]:
                        dp[3][j] = max(dp[3][j],dp[i][k]+1)

        res = 0
        for item in dp:
            for a in item:
                res = max(res,a)
        return res


if __name__ == '__main__':
    n = int(input())
    a = [int(a) for a in input().split()]
    b = [int(a) for a in input().split()]
    c = [int(a) for a in input().split()]
    d =[a,b,c,[item for item in c]]
    s = Solution()
    res = s.find(d)
    print(res,end='')
