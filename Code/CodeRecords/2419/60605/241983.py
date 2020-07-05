# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

t = list(input().strip())
mul = 1
for i in t:
    mul *= int(i)
ssum = 0
for i in t:
    ssum += int(i)
    
print(mul - ssum)