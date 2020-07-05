n = int(input())
matrix = []
for i in range(3):
    matrix.append(list(map(int, input().split(","))))

t = int(input())
found = False
for i in range(3):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == t:
            found = True
            print("True")

if not found:
    print("False")

