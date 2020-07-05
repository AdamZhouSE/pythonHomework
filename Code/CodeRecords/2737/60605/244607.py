# 题目描述
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
#
# 输入描述
# 给定一个大小为 n 的数组
# 输出描述
# 找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

li = list(eval(input()))
out = []
import collections
c = collections.Counter(li)
n = len(li)
n = int(n/3)
for i in c.items():
    if i[1]>n:
        out.append(i[0])
print(out)