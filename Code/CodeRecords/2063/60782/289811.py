"""
题目描述
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
"""
输入描述
    整数
"""
"""
输出描述
    True or False
"""
a = input()
L = len(a)
flag = True
for i in range(1, L // 2):
    if a[i - 1] != a[len(a) - i - 1]:
        flag = False
        break
print(flag)