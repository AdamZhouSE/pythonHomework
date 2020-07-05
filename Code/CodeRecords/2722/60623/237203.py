# 给定一个整数N，您必须确定它是否是Anshuman的最爱。
#
# 如果是，则打印“YES”，否则打印“NO”。
#
# 如果数字是整数5的和或差，则它是Anshuman的最爱。（5 + 5、5 + 5 + 5、5-5、5-5-5 + 5 + 5…..）
size=int(input())
a=0
while a<size:
	b=input()
	if b[-1]=='5' or b[-1]=='0':
		print("YES")
	else:
		print("NO")
	a=a+1