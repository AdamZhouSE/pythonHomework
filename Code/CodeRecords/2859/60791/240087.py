n = int(input())
list1 = []
i = 0
try:
    while True:
        inp = input()
        list1.append(inp)
except EOFError:
    pass
result = 'YES'

for i in range(n-1):
	if(list1[i][i] != list1[i][n-i-1] or list1[i+1][i+1] != list1[i][i]):
		result = 'NO'
		break
	for m in range(n-1):
		if(i != m and i != n-m-2 and i!=m+1 and i != n-m-1):
			if(list1[i][m] != list1[i][m+1]):
				result = 'NO'
				break
		if(m != 0):
			if(list1[0][1] != list1[m][0]):
				result = 'NO'
				break
for i in range(1,n-2):
		if(list1[n-1][i] != list1[n-1][i+1]):
			result = 'NO'			
if(result == 'YES'):
	if(list1[n-1][0] != list1[0][0]):
		print('NO')
	else:
		print(result)
else:
	print(result)

