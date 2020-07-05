def maximalRectangle(matrix) -> int:
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    max_area = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        for j in range(n + 1):
            while height[j] < height[stack[-1]]:
                h = height[stack.pop()]
                w = j - 1 - stack[-1]
                max_area = max(max_area, h * w)
            stack.append(j)
    return max_area
zc=[]
c=input()
c=input()
while c!="]":
    zc.append(c)
    c=input()
matrix=[]
for i in range(len(zc)):
    zc2=[]
    for j in range(len(zc[i])):
        if zc[i][j]=='0' or zc[i][j]=='1':
            zc2.append(zc[i][j])
    matrix.append(zc2)
print(maximalRectangle(matrix))





















