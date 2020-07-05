a = eval(input())
line = len(a)
row = len(a[0])
for i in range(0,row):
	length = min(line,row - i)-1
	while(length >= 0):
		for n in range(length):
			if(a[n][n+i] > a[n+1][n+1+i]):
				temp = a[n][n+i]
				a[n][n+i] = a[n+1][n+1+i]
				a[n+1][n+1+i] = temp
		length-=1
for i in range(0,line):
	length = min(line-i,row)-1
	while(length>=0):
		for n in range(length):
			if(a[n+i][n] > a[n+1+i][n+1]):
				temp = a[n+i][n]
				a[n+i][n] = a[n+1+i][n+1]
				a[n+i+1][n+1] = temp
		length-=1
print(a)