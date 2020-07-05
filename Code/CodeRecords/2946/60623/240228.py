# 从前有很多个硬币摆在一行，有正面朝上的，也有背面朝上的。正面朝上的用1表示，背面朝上的用0表示。
# 现在要求从这行的第一个硬币开始，将前若干个硬币一起翻面，问如果要将所有硬币翻到正面朝上，最少要进行这样的操作多少次？
a=input()
i=0
result=0
while i<len(a):
	if i==len(a)-1:
		break
	if a[i+1]!=a[i]:
		result+=1
	i+=1
if a[-1]=='0':
	result+=1
print(result)