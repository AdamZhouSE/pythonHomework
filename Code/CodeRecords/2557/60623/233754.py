size=int(input())
a=0
strList=[]
while a<size:
	b=input()
	strList.append(b)
	a=a+1
i=0
while i<len(strList):
	result = strList[i][0]
	j=0
	while j<len(strList[i]):
		if j==len(strList[i])-1:
			break
		if strList[i][j+1]==strList[i][j]:
			j=j+1
			continue
		else:
			result=result+strList[i][j+1]
		j=j+1
	print(result)
	i=i+1
