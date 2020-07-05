'''
给定两个分别为大小N和M的数组A和B。任务是在这两个数组之间找到并集。 可以将两个数组的并集定义为包含两个数组中不同元素的集合。
如果存在重复，则只应合并打印一次元素。
'''


def isIn(temp, res):
    for i in range(0, len(res)):
        if temp == res[i]:
            return True
    return False


def getUnion(m, n, A, B):
    res = []
    for i in range(0, len(A)):
        if isIn(A[i], res):
            continue
        else:
            res.append(A[i])
    for j in range(0, len(B)):
        if isIn(B[j], res):
            continue
        else:
            res.append(B[j])
    print(len(res))


t = int(input())
for i in range(0, t):
    num = input().split(' ')
    m = int(num[0])
    n = int(num[1])
    A = input().split(' ')
    B = input().split(' ')
    getUnion(m, n, A, B)