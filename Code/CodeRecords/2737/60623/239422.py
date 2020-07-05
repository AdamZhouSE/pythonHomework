#给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
a=input()[1:-1]
l=a.split(',')
size=len(l)
d={}
i=0
while i<size:
	if l[i] in d.keys():
		d[l[i]]=d[l[i]]+1
	else:
		d[l[i]]=1
	i=i+1
result=[]
for key,value in d.items():
	if(value>(size//3)):
		result.append(key)
j=0
while j<len(result):
	result[j]=int(result[j])
	j=j+1
print(result)