matrix = []
line = [int(x) for x in input().split(" ")]
m = len(line)
matrix.append(line)
try:
    while True:
        line = input()
        line = [int(x) for x in line.split(" ")]
        matrix.append(line)
except EOFError:
    pass
n = len(matrix)
base = 0
count = 0
while count != n*m:
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] <= base:
                count += 1
                continue
            ava = False
            if j-1 >= 0:
                if matrix[i][j-1] == base:
                    ava = True
            if j+1 < m:
                if matrix[i][j+1] == base:
                    ava = True
            if i-1 >= 0:
                if matrix[i-1][j] == base:
                    ava = True
            if i+1 < n:
                if matrix[i+1][j] == base:
                    ava = True
            if not ava:
                matrix[i][j] += 1
            else:
                count += 1
    base += 1
for lst in matrix:
    first = True
    for i in lst:
        if first:
            print(i, end="")
            first = False
        else:
            print(" ", end="")
            print(i, end="")
    print()
