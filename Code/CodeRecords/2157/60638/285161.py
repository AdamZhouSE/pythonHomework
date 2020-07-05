def change( s):
	sum = 0
	for i in range(0,len(s)) :
		if (s[i] == 'M'):
			sum = sum + 1000
		
		if (s[i] == 'D') :
			sum = sum + 500
		
		if (s[i] == 'C') :
			sum = sum + 100
		
		if (s[i] == 'L') :
			sum = sum + 50
		
		if (s[i] == 'X') :
			sum = sum + 10
		
		if (s[i] == 'V') :
			sum = sum + 5
		
		if (s[i] == 'I') :
			sum = sum + 1
		
	
	for i in range(0,len(s)-1) :
		if (s[i] == 'C') :
			if (s[i + 1] == 'D' or s[i + 1] == 'M') :
				sum = sum - 200
			
		
		if (s[i] == 'X') :
			if (s[i + 1] == 'L' or s[i + 1] == 'C') :
				sum = sum - 20
			
		
		if (s[i] == 'I') :
			if (s[i + 1] == 'X' or s[i + 1] == 'V') :
				sum = sum - 2
			
		
	
	return sum

roma=input()
print(change(roma))