# 「无零整数」是十进制表示中 不含任何 0 的正整数。
# 给你一个整数 n，请你返回一个 由两个整数组成的列表 [A, B]，满足：
# A 和 B 都是无零整数
# A + B = n
# 如果存在多个有效解决方案，你需要递增返回其中一个。
def f(n):
	s=str(n)
	for i in s:
		if i=='0':
			return True
	return False


num=int(input())
i=0
while i<=num//2:
	if f(i) or f(num-i):
		i+=1
		continue
	else:
		print("["+str(i)+","+str(num-i)+"]")
		break
