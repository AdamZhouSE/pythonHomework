A = [int(i) for i in input().split()]
B = set(A)
leg = 0
nose = 0
body = 0
if(len(B) > 4):
	print('Alien')
elif(len(B) == 1):
	print('Elephant')
else:
	for b in B:
		count = 0
		for a in A:
			if(b == a):
				count += 1
		if(count == 4):
			leg = b
		elif(count == 2):
			nose = body = b
		if(count == 5):
			leg = b
			nose = body = 0
			
	if(leg != 0):
		if(nose == body and nose == 0):
			print('Bear') 
		else:
			print('Elephant')
	else:
		print('Alien')
         

