# 给定两个表示两个整数值的二进制字符串，请找到两个字符串的乘积。例如，如果第一位字符串为“ 1100”，第二位字符串为“ 1010”，则输出应为120
size=int(input())
a=0
while a<size:
	l=input().split()
	aT=int(l[0],2)
	bT=int(l[1],2)
	result=aT*bT
	print(result)
	a=a+1