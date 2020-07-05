def maxSize(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    left = [0]*n
    right = [n]*n
    height = [0]*n
    maxArea = 0
    for i in range(m):
        curleft = 0
        curright = n
        for j in range(n):
            if matrix[i][j] == '"1"':
                height[j] = height[j]+1
            else:
                height[j] = 0
        for j in range(n):
            if matrix[i][j] == '"1"':
                left[j] = max(left[j], curleft)
            else:
                left[j] = 0
                curleft = j + 1
        for j in range(n-1,-1,-1):
            if matrix[i][j] == '"1"':
                right[j] = min(right[j], curright)
            else:
                right[j] = n
                curright = j
        for j in range(n):
            maxArea = max(maxArea, height[j]*(right[j]-left[j]))
    return maxArea

str = input()
str = input()
temp = []
while str != "]":
    i = -1
    if str.endswith(","):
        i = -2
    str = str[3:i].split(",")
    temp.append(str)
    str = input()
print(maxSize(temp))
