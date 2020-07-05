# 小佩蒂娅在家里组织了一个新年聚会，邀请了 n 个朋友来，朋友间要互相交换礼物。她藏起了她的礼物，并观察朋友们相互送礼物，她记住了谁给谁礼物，且每个人都只获得了一个礼物。
# 现在小佩蒂娅想知道每个朋友的礼物分别是谁送的，请你帮助她。
a=input()
l=input().split()
d={}
i=0
while i<len(l):
	d[i+1]=int(l[i])
	i+=1
resultList=sorted(d.items(),key=lambda item:item[1])
result=""
for val in resultList:
	result=result+str(val[0])+" "
print(result.strip())