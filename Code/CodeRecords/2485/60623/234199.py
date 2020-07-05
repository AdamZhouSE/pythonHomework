# 给定一个单词数组，按排序顺序（计数的递增顺序）一起打印所有字符相同组的计数。
# 例如，如果给定的数组是{“ cat”，“ dog”，“ tac”，“ god”，“ act”}，则分组的字谜是“（dog，god）（cat，tac，act）”。因此输出为2 3
size=int(input())
a=0
while a<size:
	b=input()#也没有用
	strList=input().split()
	i=0
	while i<len(strList):
		l=list(strList[i])
		#列表的sort是针对自己，而字典的sort则是返回一个排好序的，但本身并没有排好序
		l.sort()
		s="".join(l)
		strList[i]=s
		i=i+1
	strList.sort()
	j=0
	k=1
	myList=[]
	while j<len(strList):
		if j==len(strList)-1:
			break
		if(strList[j]==strList[j+1]):
			k=k+1
		else:
			myList.append(k)
			k=1
		j=j+1
	myList.append(k)
	myList.sort()
	m=0
	while m<len(myList):
		if m!=len(myList)-1:
			print(""+myList[m]+" ", end='')
		else:
			print(myList[m])
		m=m+1
	a=a+1