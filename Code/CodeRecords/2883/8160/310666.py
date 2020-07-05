first = input()
n, m = first.split(" ")
n = int(n)
m = int(m)
arr = []
for i in range(n):
    arr.append(input())
startI = 0
startJ = 0
find = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            # print(str(i) + " " + str(j))
            startI = i
            startJ = j
            find = True
            break
    if find:
        break

endI = 0
endJ = 0
for i in range(startI, n):
    if arr[i][startJ] == 'B':
        endI = i
    else:
        break
for j in range(startJ, m):
    if arr[startI][j] == 'B':
        endJ = j
    else:
        break

indexI = (startI+1 + endI+1) / 2
indexJ = (startJ+1 + endJ+1) / 2
print(str(int(indexI)) + " " + str(int(indexJ)))

