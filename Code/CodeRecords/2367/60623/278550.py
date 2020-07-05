a=int(input())
resultStr="1"
if a%2==0 or a%5==0:
	print(-1)
else:
	while int(resultStr)%a!=0:
		resultStr+="1"
	print(len(resultStr))