# 题目描述
# 给你一个由n个非负整数组成的数列 a_1，a_2，...，a_n。
# 你将要一个一个摧毁这个数列中的数。并且，现在给你一个由 1 到 n 组成的序列来告诉你每个数被摧毁的时间顺序。
# 每当一个元素被摧毁时，你需要找到这个当前数列中的未被摧毁的数组成的和最大的连续子序列，另外，如果当前剩余的序列是空的的话，最大和就是0。


# def build(tree: [int], ori: [int], l: int, r: int, pos: int):
#     if l == r:
#         tree[pos] = ori[l-1]
#         return
#     mid = (l + r) // 2
#     build(tree, ori, l, mid, 2*pos+1)
#     build(tree, ori, mid+1, r, 2*pos+2)
#     tree[pos] = tree[2*pos+1]+tree[2*pos+2]
#
# def update(tree: [int], l: int, r: int, pos: int, where: int):
#     if l == r:
#         if l == where:
#             # print(where, l, r, pos)
#             tree[pos] = -1
#         return
#     if l <= where <= r:
#         tree[pos] = -1
#         mid = (l + r) // 2
#         update(tree, l, mid, 2*pos+1, where)
#         update(tree, mid+1, r, 2*pos+2, where)
#
# def queryMax(tree: [int], l: int, r: int, pos: int) -> int:
#     if l == r:
#         return tree[pos]
#     mid = (l + r) // 2
#     if tree[pos] != -1:
#         return tree[pos]
#     return max(queryMax(tree, l, mid, 2*pos+1), queryMax(tree, mid+1, r, 2*pos+2))


if __name__ == '__main__':
    n = int(input())
    x1 = input().strip().split()
    x2 = input().strip().split()
    nums = []
    destroy = []
    for i in range(n):
        nums.append(int(x1[i]))
        destroy.append(int(x2[i]))
    for i in destroy:
        nums[i-1] = -1
        maxCon = -1
        begin = 0
        t = 0
        while begin < n:
            if nums[begin] >= 0:
                t += nums[begin]
                begin += 1
            else:
                maxCon = max(t, maxCon)
                t = 0
                begin += 1
        if t != 0:
            maxCon = max(maxCon, t)
        if maxCon == -1: maxCon = 0
        print(maxCon)
