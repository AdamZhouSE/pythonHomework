n = int(input())
if(n == 1):
    print(1)
else:
	result =  0
	t = False
	temp = n
	for i in range(n-1):
		if(i%4 == 0):
			temp = temp*(n-i-1)
		elif(i%4 == 1):
			if(t):
				temp = int(temp/(n-i-1))
				result -= temp
			else:
				temp = int(temp/(n-i-1))
				result += temp
			t = False
		elif(i%4 == 2):
			result += n-i-1
		else:
			t = True
			temp = n-i-1
	if(t):
		result -= temp
		
	print(result)
