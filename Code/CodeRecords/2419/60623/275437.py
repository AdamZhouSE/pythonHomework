# 给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
num=input()
mul=1
an=0
for i in num:
	mul*=int(i)
	an+=int(i)
print(mul-an)