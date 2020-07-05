'''
给你一个仅由数字 6 和 9 组成的正整数 num。
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
请返回你可以得到的最大数字。
'''

num = int(input())
x = list(str(num))
for i in range(len(x)):
    if x[i] == '6':
        x[i] = '9'
        break
res = int(''.join(x))
print(res)