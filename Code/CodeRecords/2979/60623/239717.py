strList=input().split()
i=0
d={}
while i<len(strList):
	d[strList[i]]=len(strList[i])
	i=i+1
t=sorted(d.items(),key=lambda item:item[1])
max=t[len(t)-1][1]
for key,value in d.items():
	if value==max:
		print(key)
		break
