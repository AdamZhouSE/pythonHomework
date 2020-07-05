a=int(input())
if a==0:
	print("0")
else:
	res = []
	while a:
		if a % 2 == 0:
			res.append('0')
			a = a // (-2)
		else:
			res.append('1')
			a = (a - 1) // (-2)
	print(''.join(res)[::-1])