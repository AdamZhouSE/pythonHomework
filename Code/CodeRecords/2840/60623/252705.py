# 罗玛的幸运数字是 4 和 7，因此任何由这两个数字组成的数都是他的幸运数。
# 罗玛现在得到了 n 个数，他想知道有多少个数中幸运数字的个数不超过 k 个。
# 例如 k = 2，[4,477,5] 中，[4,5] 两个数的幸运数字为 [1,0] 不超过两个，而 477 有三个。
tempList=input().split()
cri=int(tempList[1])
strList=input().split()
result=0
for var in strList:
	i=0
	temp=0
	while i<len(var):
		if var[i]=='4' or var[i]=='7':
			temp+=1
		i+=1
	if temp<=cri:
		result+=1
print(result)