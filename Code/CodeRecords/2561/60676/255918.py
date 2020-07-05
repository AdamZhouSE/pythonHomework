# 给定两个元素大小为N x N的矩阵mat1和mat2。给定值x。问题是要计算两个矩阵之和等于x的所有对。


def get_pairs(l1, l2, x):
    count = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if int(l1[i]) + int(l2[j]) == x:
                count += 1
    return count


result = []
for i in range(int(input())):
    t = input().split()
    size = int(t[0])
    x = int(t[1])
    lis1 = []
    lis2 = []
    for j in range(size):
        lis1.extend(input().split())
    for j in range(size):
        lis2.extend(input().split())
    result.append(get_pairs(lis1, lis2, x))
for i in range(len(result)):
    print(result[i])