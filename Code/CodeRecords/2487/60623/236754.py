# 给定一次选举中候选人的姓名数组（由小写字母组成）。数组中的候选人名称表示对候选人的投票。打印获得最高票数的候选人的姓名。如果有平局，则按字典顺序打印较小的名称。
size=int(input())
a=0
while a<size:
	b=input()
	l=input().split()
	l.sort()
	i=1
	d={}
	d[l[0]]=1
	while i<=len(l)-1:
		if l[i]==l[i-1]:
			d[l[i]]=d[l[i]]+1
		else:
			d[l[i]]=1
		i=i+1
	sorted(d.items(),key=lambda item:item[1],reverse=True)
	# print(d)
	for (key,value) in d.items():
		h=str(value)
		print(key+" "+h)
		break
	a=a+1