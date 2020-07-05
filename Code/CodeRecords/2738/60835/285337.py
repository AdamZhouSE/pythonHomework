class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n+1)
        max_area = 0
        for row in matrix:
            # 计算h
            for i in range(n):
                height[i] = height[i]+1 if row[i]=='1' else 0
            # 找出所有h和w的组合 
            stack = [-1]
            for j in range(n + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - 1 - stack[-1]
                    max_area = max(max_area, h * w)                
                stack.append(j)            
        return max_area

s = Solution()
m = ""
tem = ""
while tem != ']':
    tem = input()
    m = m + tem
#matrix = eval(m)
print(matrix)
print(s.maximalRectangle(matrix))
