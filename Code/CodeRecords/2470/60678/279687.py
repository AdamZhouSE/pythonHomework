def rotate(arr):
    row = len(arr)
    col = len(arr[0])
    tempArr = []
    for i in range(col):
        tempArr.append([])
        for j in range(row):
            tempArr[i].append(arr[row - j - 1][i])
    temp = []
    for i in range(col):
        temp += tempArr[i]
    print(' '.join(temp),end = " \n")

n = int(input())
for looptime in range(n):
    length = int(input())
    rec = input().split()
    arr = []
    for row in range(length):
        arr.append(rec[row * length : row * length + length])
    rotate(arr)