class Solution:
    def find(self, n):
        data = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i==0 or j==0:
                    data[i][j]=1
                else:
                    data[i][j]=data[i-1][j]+data[i][j-1]
                            
        return data[n-1][n-1]


if __name__ == '__main__':
    n = int(input())
    s = Solution()
    re = s.find(n)
    print(re)
