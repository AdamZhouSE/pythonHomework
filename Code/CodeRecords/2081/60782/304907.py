"""
题目描述

这是一道模板题。

给定一个字符串A和一个字符串B ，求B 在A中的出现次数。A 和B 中的字符均为英语大写字母或小写字母。

A 中不同位置出现的B 可重叠。

输入描述

输入共两行，分别是字符串A和字符串B 。

输出描述

输出一个整数，表示 B 在A 中的出现次数。
"""
s = list(input())
num = []
# 将字符串转换为没有重复的列表并排序方便与后面压缩字典对应
no_repeat_s = list(set(s))
no_repeat_s.sort()
# 统计每个字母的个数
for i in no_repeat_s:
    num.append(s.count(i))
# 将字母与其对应出现的次数压缩成字典
dict_s = dict(zip(no_repeat_s, num))
# 初始总长度和flag flag 用于检测是否有单个的字符
total = 0
flag = 0
# 如果字符串中有字符出现偶数次，那么可以全拿出来拼接
# 如果字符串中有字符出现奇数次，那么可以拿出 n-1 个来拼接
# 注：如果发现有奇数次的话：
#     总字符数如果是奇数，说明最后可以放任意多余的字符在中间的位置
#     总字符数如果是偶数的话，那应该还有一个奇数串，所以最后也可以放一个多余的字符在中间的位置
for i in no_repeat_s:
    if dict_s[i] % 2 == 0:
        total += dict_s[i]
    else:
        flag = 1
        total += dict_s[i] - 1
if flag == 1:
    print(total + 1)
else:
    print(total)
