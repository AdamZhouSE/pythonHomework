size=int(input())
a=0
strList=[]
while a<size:
	b=input()
	strList.append(b)
	a=a+1
i=0
while i<len(strList):
	l = list(strList[i])
	l.sort()
	s="".join(l)
	j=0
	while j<len(s):
		if j==len(s)-1:
			print(1)
			break
		if s[j+1]==s[j]:
			print(0)
			break
		j=j+1

	i=i+1
