"""
题目描述

给定一个字符串S，该字符串由左括号“（”和“）”组成。查找最长的有效括号子字符串的长度。

输入描述

第一行包含测试用例T的数量。每个测试用例都有一个字符串N，长度为'（'和'）'。

输出描述

输出最长的有效括号子字符串的长度
"""
times = int(input())
while times > 0:
    times -= 1
    answer = 0
    num_l = 0
    num_r = 0
    cur_len = 0
    inp = list(input())
    for i in inp:
        if inp == '(':
            num_l += 1
            cur_len += 1
        if inp == ')':
            num_r += 1
            cur_len += 1
        if num_r > num_l:
            if answer < cur_len:
                answer = cur_len
            cur_len = 0
            num_r = 0
            num_l = 0
    if answer < cur_len:
        answer = cur_len
    print(answer)