a=int(input())
resultStr="1"
if a==2 or a==4 or a==5 or a==6 or a==8:
	print(-1)
else:
	while int(resultStr)%a!=0:
		resultStr+="1"
	print(len(resultStr))