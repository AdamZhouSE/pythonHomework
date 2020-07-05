# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
tempList=input().split(',')
l1=[]
for i in tempList:
	l1.append(int(i))
s=input()
l2=[]
if len(s)==1:
	l2.append(int(s))
else:
	tem=s.split(',')
	for i in tem:
		l2.append(int(i))
i=0
while True:
	signal=0
	l=[]
	for var in l2:
		j=var-i
		while j<=var+i:
			l.append(j)
			j+=1
	for var in l1:
		if var not in l:
			i+=1
			signal+=1
			break
	if signal==0:
		print(i)
		break
