class Solution(object):
    def maxSideLength(self, mat, threshold):
        row = len(mat)
        col = len(mat[0])

        P = self.PrefixM(mat, row, col)

        res = 2
        ans = 0  
        for c in range(1, col + 1):
            for r in range(1, row + 1):
                cmax = min(col + 1 - c, row + 1 - r)
                for n in range(res, cmax + 1): 
                    S = P[r + n - 1][c + n - 1] - P[r - 1][c + n - 1] - P[r + n - 1][c - 1] + P[r - 1][c - 1]
                    if S > threshold:
                        break
                    if S <= threshold and n >= res:
                        res = n
                        ans = n
        return ans

    def PrefixM(self, mat, row, col):
        P = [[0 for i in range(col + 1)] for j in range(row + 1)]
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                P[r][c] = mat[r - 1][c - 1] + P[r - 1][c] + P[r][c - 1] - P[r - 1][c - 1]
        return P



count = int(input())
mat = []
for i in range(count):
    read = input()
    nums = read.split(',')
    nums = [int(nums[i]) for i in range(len(nums))]
    mat.append(nums)
threshold = int(input())
t = Solution()
print(t.maxSideLength(mat, threshold))