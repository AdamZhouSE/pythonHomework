def find(x,y,limit):
    res = 0
    for i in range(x, len(matrix)):
        for j in range(y, len(matrix[0])):
            # 计算和
            s = 0
            for k in range(x, i+1):
                s+=sum(matrix[k][y:j+1])
            if s <= limit:
                res = max(s, res)
    return res



n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split(','))))
k = int(input())

max_sum = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        max_sum = max(max_sum,find(row,col,k))
print(max_sum)