'''
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
'''

n = int(input())
add = 0
mul = 0
while n>0:
    digit = n%10
    n //= 10
    add += digit
    mul *= digit
res = mul - add
print(res)