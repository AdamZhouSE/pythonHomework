# 佩奇和他的小伙伴正沿着高度 h 的围墙走，他们不希望围墙外的门卫注意到他们。 为了躲过门卫大爷，每个小伙伴的身高不能超过围墙的高度 h。
# 第 i 个人的身高等于 a[i]。 如果一个人的身高超过了 h，他可以弯腰，那么他就不会被大爷注意到。
# 假定平常走路的人的宽度等于 1，而弯腰的人的宽度等于 2。 他们想并排行走。 请问道路的最小宽度是多少时，他们可以连续走而不会被门卫大爷注意到？
aList=input().split()
bList=input().split()
h=int(aList[1])
result=len(bList)
for temp in bList:
	if int(temp)>h:
		result+=1
print(result)