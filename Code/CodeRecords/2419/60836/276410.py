"""
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差
"""

s=[int(m) for m in list(str(input()))]

mul=1
add=0
for i in s:
    mul*=i
    add+=i

print(mul-add)