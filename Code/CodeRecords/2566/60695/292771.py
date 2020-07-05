n = int(input())
matrix = []
for i in range(n):
    a = input()
    a = list(map(int, a.split(",")))
    matrix.append(a)
row, col = len(matrix), len(matrix[0])
mem = [[0] * col for _ in range(row)]

for i in range(row - 1, -1, -1):
    for j in range(col - 1, -1, -1):
        if i == row - 1 and j == col - 1:
            mem[i][j] = max(0, -matrix[i][j])
        elif i == row - 1:
            mem[i][j] = max(0, mem[i][j + 1] - matrix[i][j])
        elif j == col - 1:
            mem[i][j] = max(0, mem[i + 1][j] - matrix[i][j])
        else:
            mem[i][j] = max(0, min(mem[i + 1][j], mem[i][j + 1]) - matrix[i][j])
print(mem[0][0]+1)