# 瓦莱拉得到了一张 n*n 的方格纸，每个单位正方形包含英语字母的一些小写字母。
# 瓦莱拉需要知道方形纸上书写的字母是否为字母“ X”。 瓦莱拉的老师认为，在下列情况下，纸上的字母形成“ X”：
# 在方格纸的两个对角线上，所有字母均相同；
# 纸张的所有其他正方形（它们不在对角线上）包含与对角线上的字母不同，但都是同一个字母。
# 帮助瓦莱拉，为他编写完成上述任务的程序。
size=int(input())
i=0
myList=[]
while i<size:
	l=list(input())
	myList.append(l)
	i+=1
str=myList[0][0]
i=0
while i<size:
	if myList[i][i]!=str:
		print("NO")
		break
	i+=1
if i==size:
	j=0
	while j<size:
		if myList[j][size-1-j]!=str:
			print("NO")
			break
		j+=1
	if j==size:
		newList=[]
		a=0
		while a<size:
			b=0
			while b<size:
				if myList[a][b] not in newList:
					newList.append(myList[a][b])
				b+=1
			a+=1
		if len(newList)>2:
			print("NO")
		else:
			print("YES")