# 题目描述
# 您会得到一个表示图像的n x n 2D矩阵。 将图像旋转90度（顺时针）。
# 您需要就地执行此操作。 请注意，如果最终使用其他数组，则只会得到部分分数。 例： 如果数组是 1 2 3 4 5 6 7 8 9 然后旋转的数组变为： 7 4 1 8 5 2 9 6 3
#
# 输入描述
# 第一行包含一个整数“ T”，表示测试用例的总数。 在每个测试案例中，第一行都包含一个整数“ N”，表示2D方阵的大小。 在第二行中，矩阵A [] []的元素以行主要形式用空格隔开。
#
# 输出描述
# 对于每个测试用例，按行打印旋转数组的元素，每个元素用空格分隔。在新行中打印每个测试用例的输出。

t = int(input())
liN = []
li = []
for i in range(t):
    liN.append(int(input()))
    li.append(input().strip().split(" "))

for i in range(t):
    n = liN[i]
    l = li[i]
    dd = {}
    res = ""
    for j in range(n):
        for k in range(n):
            res = res + l[(n-1-k)*n+j] + " "
    print(res)