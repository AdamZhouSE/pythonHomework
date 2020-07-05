t = int(input())
matrix = list()
for i in range(0, t):
    num = list(map(int, input().split(',')))
    matrix.append(num)
flag = 'False'
target = int(input())
for i in range(0,t):
    if matrix[i][len(matrix[i])-1]>=target:
        for j in matrix[i]:
            if j == target:
                flag = 'True'

print(flag) 