"""
给你一个仅由数字 6 和 9 组成的正整数 num
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6
请返回你可以得到的最大数字
"""

arr=list(str(input()))

for i in range(len(arr)):
    if arr[i]=='6':
        arr[i]='9'
        break

print(int("".join(arr)))