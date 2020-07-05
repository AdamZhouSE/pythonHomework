# 奥尔加来看望双胞胎安娜和玛丽亚，看到他们有许多饼干，饼干被分到袋子里。
# 因为有很多饼干，奥尔加决定偷一包。不过，她不希望姐妹俩在分饼干时无缘无故吵架。这就是为什么奥尔加想偷一包饼干，这样剩下的袋子里的饼干数量可以平均地分成两份。
# 请问有多少种偷一袋饼干的方法，这样剩下的袋子里的饼干总数是偶数？
size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
all=0
for var in intList:
	all+=var
result=0
if all%2==0:
	for i in intList:
		if i%2==0:
			result+=1
	print(result)
else:
	for i in intList:
		if i%2==1:
			result+=1
	print(result)