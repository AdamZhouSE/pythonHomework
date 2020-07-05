c = input()
line = input()
line = list(map(int, line[3:len(line) - 2].split(",")))
matrix = []
matrix.append(line)
for i in range(0, len(line) - 2):
    line = input()
    line = list(map(int, line[3:len(line) - 2].split(",")))
    matrix.append(line)
line = input()
line = list(map(int, line[3:len(line) - 1].split(",")))
matrix.append(line)
dic = {}
mpath = 1
line = len(matrix)
col = len(matrix[0])
for i in range(line):
    for j in range(col):
        dic[(i, j)] = matrix[i][j]
val = dic.keys()
nums1 = [[1 for i in range(col)] for j in range(line)]
dic = sorted(dic.items(), key=lambda x: x[1])
for item in dic:
    i = item[0][0]
    j = item[0][1]
    if (i + 1, j) in val and matrix[i + 1][j] < matrix[i][j] and nums1[i][j] < nums1[i + 1][j] + 1:
        nums1[i][j] = nums1[i + 1][j] + 1
    if (i - 1, j) in val and matrix[i - 1][j] < matrix[i][j] and nums1[i][j] < nums1[i - 1][j] + 1:
        nums1[i][j] = nums1[i - 1][j] + 1
    if (i, j + 1) in val and matrix[i][j + 1] < matrix[i][j] and nums1[i][j] < nums1[i][j + 1] + 1:
        nums1[i][j] = nums1[i][j + 1] + 1
    if (i, j - 1) in val and matrix[i][j - 1] < matrix[i][j] and nums1[i][j] < nums1[i][j - 1] + 1:
        nums1[i][j] = nums1[i][j - 1] + 1
    mpath = max(mpath,nums1[i][j])
print(mpath)