# 给定一个字符串str和另一个字符串patt。在str中的最小索引处找到patt中的字符。如果str中不存在patt字符，则打印$
size=int(input())
a=0
while a<size:
	firstStr=input()
	SecondStr=input().split()
	i=0
	signal=False
	while i<len(firstStr):
		if(firstStr[i] in SecondStr):
			print(firstStr[i])
			signal=True
			break
		i=i+1
	if not signal:
		print("$")
	a=a+1