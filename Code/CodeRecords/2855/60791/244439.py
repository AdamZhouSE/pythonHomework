n = int(input())
x = n
plate = []
while(x>0):
    x-=1
    plate.append(str(input()))
result = True
for a in range(n):
	if(n==1):
		result = True
		break
	for b in range(n):
		count_o = 0
		if(a==0 and b==0):
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(a==n-1 and b==0):
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(a==0 and b==n-1):
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(a==n-1 and b==n-1):
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(a==0):
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(a==n-1):
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break		
		elif(b==0):
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		elif(b==n-1):
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
		else:
			if(plate[a-1][b]=='o'):
				count_o += 1
			if(plate[a][b+1]=='o'):
				count_o += 1
			if(plate[a+1][b]=='o'):
				count_o += 1
			if(plate[a][b-1]=='o'):
				count_o += 1
			if(count_o%2 != 0):
				result = False
				break
	if(result == False):
		break	
if(result):
    print("YES")
else:
    print("NO")