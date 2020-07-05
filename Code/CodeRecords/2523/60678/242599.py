matrix = eval(input())
row = len(matrix)
col = len(matrix[0])


def sortLine(startRow, startCol):
    sortedList = []  # 记得要更新归零
    if startRow >= startCol:
        # 行数率先触底就结束
        for i in range(0, row - startRow):
            sortedList.append(matrix[startRow + i][startCol + i])
        sortedList.sort()
        for i in range(0, row - startRow):
            # 进行赋值
            matrix[startRow + i][startCol + i] = sortedList[i]
        sortedList = []
    else:
        # 列数率先触底就结束
        for i in range(0, col - startCol):
            sortedList.append(matrix[startRow + i][startCol + i])
        sortedList.sort()
        for i in range(0,  col - startCol):
            matrix[startRow + i][startCol + i] = sortedList[i]
        sortedList = []


for i in range(0, row):
    sortLine(i, 0);
for i in range(0, col):
    sortLine(0, i)
print(matrix)