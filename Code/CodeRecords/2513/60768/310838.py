n = int(input())
matrix = []
for i in range(n):
    temp = [int(i) for i in input().split(',')]
    matrix.append(temp)
k = int(input())
re = [matrix[0][0]]
for i in range(n):
    for j in range(n):
        if i != 0 or j != 0:
            for t in range(len(re)):
                if re[t] > matrix[i][j]:
                    re.insert(t, matrix[i][j])
                    break
            else:
                re.append(matrix[i][j])
print(re[k - 1])