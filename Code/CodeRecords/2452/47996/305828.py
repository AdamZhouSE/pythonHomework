n = (int(input()))
str = input()
firstLine = str.split(",")
firstLine = [int(x) for x in firstLine]
m = len(firstLine)
matrix = [[0 for i in range(m)] for j in range(n)]
for i in range(m):
    matrix[0][i] = firstLine[i]
for j in range(1,n):
    str = input()
    line = str.split(",")
    line = [int(x) for x in line]
    for i in range(m):
        matrix[j][i] = line[i]
target = int(input())
if target < matrix[0][0] or target > matrix[n-1][m-1]:
    print("False")
else:
    tempM = 0
    tempN = n-1
    while tempN >= 0 and tempM < m:
        if target == matrix[tempN][tempM]:
            print("True")
            break
        elif target < matrix[tempN][tempM]:
            tempN -= 1
        else:
            tempM += 1
    if tempN < 0 or tempM >= m:
        print('False')
