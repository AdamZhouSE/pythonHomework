n,d = map(int,input().split())
for i in range(int(input())):
	x,y = map(int,input().split())
	if ((-1)*d <= y-x <= d) and (d <= y+x <= 2*n-d):
		print('YES')
	else:
		print('NO')