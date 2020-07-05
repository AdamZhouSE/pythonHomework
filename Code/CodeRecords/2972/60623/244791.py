# LW有两个字符串s和t。
# 在每个步骤中，LW都可以选择s的任意字符c，并在其后插入任何字符d（d≠c）。
# LW希望将s转换为t。但是有可能吗？
a=int(input())
for i in range(a):
	aStr=input()
	bStr=input()
	if len(aStr)>len(bStr):
		print("No")
	elif len(aStr)==len(bStr):
		if aStr==bStr:
			print("Yes")
		else:
			print("No")
	else:
		j=0
		while j<len(bStr):
			if j>len(aStr)-1:
				aStr = aStr[0:j] + bStr[j] + aStr[j:]
				j+=1
				continue
			if aStr[j]==bStr[j]:
				j+=1
				continue
			else:
				if aStr[j-1]==bStr[j]:
					# if bStr=="aapple":
					# 	print("No")
					# else:
					# 	print(aStr)
					# 	print(bStr)
					# 	print("No")
					x=j-1
					while aStr[x]==bStr[j] and x>=0:
						x-=1
					if x<0:
						print("No")
					else:
						aStr = aStr[0:x+1] + bStr[j] + aStr[x+1:]
					break
				else:
					aStr=aStr[0:j]+bStr[j]+aStr[j:]
					j+=1
		if aStr==bStr:
			print("Yes")