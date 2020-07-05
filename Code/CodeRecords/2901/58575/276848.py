number=int(input())
flag=True
while number!=0:
	if number%2==number//2%2:
		flag=False
		break
	number=number//2

print(flag)