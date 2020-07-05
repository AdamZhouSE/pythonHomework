# 桌子上有 n 个石头排成一排，可能为红色，绿色和蓝色，请你移除最少数量的石头使得相邻石头的颜色均不同。
size=int(input())
l=list(input())
i=0
result=0
while i<len(l):
	if i==len(l)-1:
		break
	else:
		if l[i+1]==l[i]:
			#删除指定索引的list
			del l[i+1]
			result+=1
			i-=1
	i+=1
print(result)