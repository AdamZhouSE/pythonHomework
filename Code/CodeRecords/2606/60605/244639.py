# 题目描述
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，
# 写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
# 输入描述
# 一共两行，分别是一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
# 你可以假设 nums 中的所有元素是不重复的。
# n 将在 [1, 10000]之间。
# nums 的每个元素都将在 [-9999, 9999]之间。
# 输出描述
# 如果目标值存在返回下标，否则返回 -1。

li = list(eval(input()))
n = int(input())
res = -1

for i in range(len(li)):
    if li[i] == n:
        res = i
        break

print(res)