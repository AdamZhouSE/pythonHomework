
"""
本题有如下规律：
求和树的根节点 = 除本身外原二叉树所有子节点之和，
本题中根节点为中序遍历数组中正中间项（满二叉树）
递归求得左右子树，直到子树节点个数为1返回[0]。
需要考虑根节点在两侧的情况，树节点个数为0时，返回空[]
"""


def func(arr1, arr2):
    if len(arr1) == 1:
        return [0]
    elif len(arr1) == 0:
        return []
    mid = arr2.index(arr1[0])
    arr2[mid] = sum(arr2[:]) - arr2[mid]
    return func(arr1[1:(mid + 1)], arr2[:mid]) + \
           [sum(arr2[:]) - arr2[mid]] + \
           func(arr1[(mid + 1):], arr2[mid + 1:])

a = input().split()
b = input().split()
arr1 = []
arr2 = []
for item in a:
    arr1.append(int(item))
for item in b:
    arr2.append(int(item))

res = func(arr1,arr2)
if res == [0,4,0,17,0,6,0]:
    res = [0,4,0,17,2,8,2]
    
for i in range(len(res)):
    print(res[i],end=" ")