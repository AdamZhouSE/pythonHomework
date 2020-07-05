#给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。
#字符串切片操作,第三个参数是步长
a=input()[1:-1]
l=a.split(',')
d={}
i=0
while i<len(l):
	if l[i] in d.keys():
		d[l[i]]=d[l[i]]+1
	else:
		d[l[i]]=1
	i=i+1
t=sorted(d.items(),key=lambda item:item[1])
print(t[0][0])