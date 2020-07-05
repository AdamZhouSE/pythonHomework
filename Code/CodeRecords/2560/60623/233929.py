#给定项目数组，第i个索引元素表示项目ID，给定数字m，则任务是删除m个元素，以使剩余的唯一ID最少。打印不同ID的数量。
size=int(input())
a=0
while a<size:
	b=input()#没什么用
	list=input().split()
	num=int(input())
	i=0
	d={}
	while i<len(list):
		if(list[i] in d):
			d[list[i]]=d[list[i]]+1
		else:
			d[list[i]]=1
		i=i+1
	#按字典里的value升序排序
	dict=sorted(d.items(),key=lambda item:item[1])
	#遍历字典每一项
	# d.items: an iterator over the (key, value) items
	h=0
	for key, value in d.items():
		if(num>=value):
			num=num-value
		else:
			h=h+1
	print(h)
	a=a+1