# 给定一个非负数N和两个值L和R。
# 问题是将N的二进制表示形式的L到R范围内的位切换，即，从最右边的L位切换到最右边的R位。切换操作将位0翻转为1，将位1翻转为0。
size=int(input())
a=0
while a<size:
	l=input().split()
	b=int(l[0])
	bStr=bin(b)
	resultStr=""
	i=0
	while i<len(bStr):
		if((i>=len(bStr)-int(l[2])) and (i<=len(bStr)-int(l[1]))):
			if(bStr[i]=="0"):
				resultStr=resultStr+"1"
			else:
				resultStr = resultStr + "0"
		else:
			resultStr=resultStr+bStr[i]
		# i=i+1
	print(int(resultStr,2))
	a=a+1