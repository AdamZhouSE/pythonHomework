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
a = input()
b = input()
count = 0;

for i in range(len(a)):
    for j in range(i, len(a) + 1):
        if a[i:j] == b:
            count += 1
print(count, end="")
