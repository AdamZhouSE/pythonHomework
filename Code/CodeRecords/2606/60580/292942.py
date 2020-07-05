a = input()[1:-1]
target = int(input())
l = a.split(',')
i = 0
isExist = False
while i < len(l):
	if int(l[i]) == target:
		print(i)
		isExist = True
		break
	i = i+1
if not isExist:
	print(-1)