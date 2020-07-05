# 肖恩要把一个 m GB 的大文件保存到一个U盘上。他有 n 个U盘，容量分别为 a1, a2, ..., an GB。假设这个大文件可以被分成任意份存储，请帮助肖恩计算最少需要的U盘数量。
a=int(input())
capacity=int(input())
l=[]
for i in range(a):
	temp=int(input())
	l.append(temp)
l.sort()
i=len(l)-1
result=0
cri=0
while i>=0:
	cri=cri+l[i]
	if cri<capacity:
		result+=1
	else:
		result+=1
		break
	i-=1
print(result)
