"""
题目描述

您将得到3个大小为N的不同数组A，B和C。

找到索引i的数量，使得： Ai = Bi + Ck

其中k可以位于[1，N]之间。

输入描述

输入的第一行包含一个整数T，表示测试用例的数量。每个测试用例的第一行包含一个整数N，它表示数组的大小。的下3行分别包含数组A，B和C的N个空格分隔的整数。

输出描述

对于每个测试用例，打印满足给定条件的该索引的数量计数。


"""

times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    C = list(map(int, input().split(" ")))
    num = 0
    for i in range(n):
        for k in range(n):
            if A[i] == B[i] + C[k]:
                num += 1
    print(num)