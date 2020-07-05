"""
题目描述
    给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
"""
n = input()
n_list = list(n)
while len(n_list) != 1:
    temp = 0
    for i in n_list:
        temp += int(i)
    tmp = str(temp)
    n_list = list(tmp)
print(n_list[0])