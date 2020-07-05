result = "Yes"
length = int(input())
matrix = ["x" * (length + 2)]
for i in range(0, length):
    matrix.append("x"+input()+"x")
matrix.append("x" * (length + 2))
for i in range(1, length + 1):
    row = matrix[i]
    for j in range(1, length + 1):
        temp_ls = [matrix[i - 1][j], matrix[i][j - 1], matrix[i][j + 1], matrix[i + 1][j]]
        if temp_ls.count('o') % 2 != 0:
            result = "No"
print(result.upper())