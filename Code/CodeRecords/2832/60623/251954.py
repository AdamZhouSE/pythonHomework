# 伊万最近买了一本侦探小说。 这本书非常有趣，以至于本书的每一页都有一个谜，稍后将对此进行解释。 第 i 页包含的一些秘密，将在第 a[i] (a[i]>=i) 页上进行解释.
# 伊万想读完整本书。 每天，他都会从未阅读过的一页开始，并继续逐页阅读，直到对他所读的所有奥秘都得到解释
# （伊万结束这一天的阅读当且仅当不存在一个下标 i，使得伊万今天读过第 i 页但没有读过第 a[i] 页）。
# 请输出伊万读完整本书所需要的天数。
size=int(input())
tempList=input().split()
pageList=[]
pageList.append(0)
for var in tempList:
	pageList.append(int(var))
i=1
result=0
while i<len(pageList):
	l=[]
	l.append(pageList[i])
	l.sort()
	while i<l[len(l)-1]:
		i += 1
		l.append(pageList[i])
		l.sort()
	result+=1
	i+=1
print(result)
