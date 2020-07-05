# 有n个学生想要去参加一个比赛，他们每个人的能力为 ai，每个学生每做一道题就能让自己的能力提升一级。
# 已知只有相同能力的人才能组队，一个队伍为两人，请问如果每个人都需要队友，那么所有人总共至少需要做多少道题才能达成条件？
size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
intList.sort()
i=0
result=0
while i<size:
	if i==size:
		break
	else:
		result=result+intList[i+1]-intList[i]
	i+=2
print(result)