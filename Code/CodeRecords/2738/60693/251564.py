input()
matrix=[]
inp=input()
while inp!=']':
    if inp[-1]==',':
        matrix.append(eval(inp[:-1]))
    else:matrix.append(eval(inp))
    inp = input()

m,n = len(matrix), len(matrix[0])
max_area=0
leftmin=[-1 for i in range(n)]
rightmin=[n for i in range(n)]
height=[0 for i in range(n)]
for row in range(m):
    for col in range(n):
        if matrix[row][col] == '1':height[col] += 1
        else:height[col] = 0

    # 更新左边的边界
    bound = -1  # 记录上一次出现0的位置
    for col in range(n):
        if matrix[row][col] == '1':
            leftmin[col] = max(leftmin[col],bound)
        else:
            leftmin[col] = -1
            bound = col
    
    # 更新右边的边界

    bound=n
    for col in range(n-1,-1,-1):
        if matrix[row][col] == '1':
            rightmin[col]=min(rightmin[col],bound)
        else:
            rightmin[col] = n
            bound = col

    for col in range(n-1,-1,-1):
        tmp = (rightmin[col]-leftmin[col]-1)*height[col]
        max_area = max(max_area,tmp)

print(max_area)