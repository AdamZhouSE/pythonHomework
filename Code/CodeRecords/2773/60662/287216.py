matrix = []
for i in range(0, 4):
    s = input()
    if 0 < i < 4:
        temp = list(map(int, s.strip('  [],').split(',')))
        matrix.append(temp)
a = len(matrix)
dic = {}
nums_max = 1
if a == 0:
    nums_max = 0
else:
    b = len(matrix[0])
    for i in range(a):
        for j in range(b):
            dic[(i, j)] = matrix[i][j]
    v = dic.keys()
    nums1 = [[1 for i in range(b)] for j in range(a)]
    dic = sorted(dic.items(), key=lambda x: x[1])
    for k in dic:
        i = k[0][0]
        j = k[0][1]
        if (i + 1, j) in v and matrix[i + 1][j] < matrix[i][j] and nums1[i][j] < nums1[i + 1][j] + 1:
            nums1[i][j] = nums1[i + 1][j] + 1
        if (i, j + 1) in v and matrix[i][j + 1] < matrix[i][j] and nums1[i][j] < nums1[i][j + 1] + 1:
            nums1[i][j] = nums1[i][j + 1] + 1
        if (i - 1, j) in v and matrix[i - 1][j] < matrix[i][j] and nums1[i][j] < nums1[i - 1][j] + 1:
            nums1[i][j] = nums1[i - 1][j] + 1
        if (i, j - 1) in v and matrix[i][j - 1] < matrix[i][j] and nums1[i][j] < nums1[i][j - 1] + 1:
            nums1[i][j] = nums1[i][j - 1] + 1
        nums_max = max(nums_max, nums1[i][j])

print(nums_max)

