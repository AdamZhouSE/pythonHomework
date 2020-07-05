# 某地铁环线有 n 个车站。 我们知道所有邻近站点之间的距离：
# d[1] 是第 1 站和第 2 站之间的距离;
# d[2] 是第 2 站和第 3 站之间的距离;
# ......
# d[n-1] 是第 n-1 和第 n 个站之间的距离;
# d[n]是第 n 个站和第 1 个站之间的距离。
# 列车沿着两个方向的环线。 找到站点 s 和 t 之间的最短距离。
num=int(input())
tempList=input().split()
busList=[]
all=0
for var in tempList:
	all+=int(var)
	busList.append(int(var))
to=input().split()
i=1
l=[]
l.append(0)
temp=0
while i<num:
	temp=temp+busList[i-1]
	l.append(temp)
	i+=1
start=int(to[0])-1
end=int(to[1])-1
if start>=end:
	start,end=end,start
path=l[end]-l[start]
if all-path>=path:
	print(path)
else:
	print(all-path)