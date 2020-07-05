n = int(input())
matrix = []
for i in range(n):
    line = input().split(',')
    matrix.append(line)
target = input()
for j in range(n):
    if target in matrix[j]:
        print("True")
        exit(0)
print("False")
    